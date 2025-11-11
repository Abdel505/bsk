from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        
        self._frames = []
        self._MAX_FRAMES = 10

    def add_frame(self, frame: Frame) -> None:
        if len(self._frames) < self._MAX_FRAMES:
            self._frames.append(frame)
        else:
            raise BowlingError("A game can only have 10 frames.")

    def get_frame_at(self, i: int) -> Frame:
        if 0 <= i < len(self._frames):
            return self._frames[i]
        raise BowlingError("Frame index out of bounds.")

    def calculate_score(self) -> int:
        pass

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
