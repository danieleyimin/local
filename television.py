class Television:
    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        # Instance variables
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._volume_before_mute: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """Turn the TV on and off."""
        self._status = not self._status

    def mute(self) -> None:
        """Mute and unmute the TV."""
        if self._status:
            self._muted = not self._muted
            if self._muted:
                self._volume_before_mute = self._volume
                self._volume = self.MIN_VOLUME
            else:
                self._volume = self._volume_before_mute

    def channel_up(self) -> None:
        """Increase the TV channel."""
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the TV channel."""
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the TV volume."""
        if self._status and not self._muted:
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease the TV volume."""
        if self._status and not self._muted:
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
        """Return a string representation of the TV object."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
