# 作りかけ
from __future__ import annotations
import pygame
import numpy as np
from actor import *
from component import *

class gravity_component(component):
    def __init__(self, owner: actor):
        super().__init__(owner)
        self.__gravity: float = 1.5

    def __del__(self):
        super().__del__()

    def process_input(self, delta_time: float):
        self._owner.velocity = np.array([self._owner.velocity[0], self._owner.velocity[1] + self.__gravity * delta_time])