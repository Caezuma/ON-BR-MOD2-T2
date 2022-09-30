from dino_runner.utils.constants import STOPWATCH, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Time(PowerUp):
    def __init__(self):
        self.image = STOPWATCH
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)