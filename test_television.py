import pytest
from television import Television

@pytest.fixture
def tv():
    return Television()

def test_init(tv):
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == tv.MIN_VOLUME
    assert tv._channel == tv.MIN_CHANNEL

def test_power(tv):
    tv.power()
    assert tv._status is True
    tv.power()
    assert tv._status is False

def test_mute(tv):
    # TV is on, volume increased once, and then muted
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted is True
    assert tv._volume == tv.MIN_VOLUME

    # TV is on and unmuted
    tv.mute()
    assert tv._muted is False

    # TV is off and muted
    tv.power()
    tv.mute()
    assert tv._muted is True
    assert tv._volume == tv.MIN_VOLUME

    # TV is off and unmuted
    tv.mute()
    assert tv._muted is False

def test_channel_up(tv):
    # TV is off and the channel has been increased
    tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL

    # TV is on and the channel has been increased
    tv.power()
    tv.channel_up()
    assert tv._channel == (tv.MIN_CHANNEL + 1) % (tv.MAX_CHANNEL + 1)

    # TV is on, and one has increased the channel past the maximum value
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert tv._channel == tv.MIN_CHANNEL

def test_channel_down(tv):
    # TV is off and the channel has been decreased
    tv.channel_down()
    assert tv._channel == tv.MIN_CHANNEL

    # TV is on and one has decreased the channel past the minimum value
    tv.power()
    tv.channel_down()
    assert tv._channel == tv.MAX_CHANNEL

def test_volume_up(tv):
    # TV is off and the volume has been increased
    tv.volume_up()
    assert tv._volume == tv.MIN_VOLUME

    # TV is on and the volume has been increased
    tv.power()
    tv.volume_up()
    assert tv._volume == (tv.MIN_VOLUME + 1)

    # TV is on, muted, and the volume has been increased
    tv.mute()
    tv.volume_up()
    assert tv._volume == (tv.MIN_VOLUME + 1)

    # TV is on and one has increased the volume past the maximum value
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    assert tv._volume == tv.MAX_VOLUME

def test_volume_down(tv):
    # TV is off and the volume has been decreased
    tv.volume_down()
    assert tv._volume == tv.MIN_VOLUME

    # TV is on and the volume has been decreased
    tv.power()
    tv.volume_up()  # Increase volume to the maximum first
    tv.volume_down()
    assert tv._volume == (tv.MAX_VOLUME - 1)

    # TV is on, muted, and the volume has been decreased
    tv.mute()
    tv.volume_down()
    assert tv._volume == tv.MIN_VOLUME

    # TV is on and one has decreased the volume past the minimum value
    tv.volume_down()
    tv.volume_down()
    tv.volume_down()
    assert tv._volume == tv.MIN_VOLUME

# Example test for __str__
def test_str(tv):
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
