import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_add_and_get_frame(self):
        game = BowlingGame()
        frame = Frame(1, 5)
        game.add_frame(frame)
        self.assertEqual(len(game._frames), 1)
        self.assertEqual(game.get_frame_at(0), frame)


    def test_get_first_and_second_throw(self):
        game = BowlingGame()
        frame = Frame(1, 5)
        game.add_frame(frame)
        self.assertEqual(game.get_frame_at(0).get_first_throw(), 1)
        self.assertEqual(game.get_frame_at(0).get_second_throw(), 5)
