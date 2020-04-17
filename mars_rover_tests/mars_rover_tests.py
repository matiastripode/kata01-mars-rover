import unittest
from unittest import mock
from parameterized import parameterized
import mars_rover.mars_rover
from mars_rover.mars_rover import MarsRover, Compass, Point, TurnCommands, MoveCommand, OutOfWorldBoundariesError

"""
Your Task
You’re part of the team that explores Mars by sending remotely controlled vehicles 
to the surface of the planet. Develop an API that translates the commands 
sent from earth to instructions that are understood by the rover.

Requirements
1. You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
2. The rover receives a character array of commands.
3. Implement commands that move the rover forward/backward (f,b).
4. Implement commands that turn the rover left/right (l,r).
5. Implement wrapping from one edge of the grid to another. (planets are spheres after all)
6. Implement obstacle detection before each move to a new square. 
7. If a given sequence of commands encounters an obstacle, the rover moves up to the last possible point, 
    aborts the sequence and reports the obstacle.

Rules
1. Hardcore TDD. No Excuses!
2. Change roles (driver, navigator) after each TDD cycle.
3. No red phases while refactoring.
4. Be careful about edge cases and exceptions. We can not afford to lose a mars rover, just because the developers overlooked a null pointer.
"""


class MarsRoverTestCase(unittest.TestCase):

    def test01_created_rover_mars_should_not_be_none(self):
        mars_rover = MarsRover(None, None)
        self.assertNotEqual(mars_rover, None)

    #Requirements
    #1. You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
    def test02_start_coordinates_should_be_same_as_passed_during_construction(self):
        x = 0
        y = 0
        start_point = Point(x,y)
        direction = Compass.N
        mars_rover = MarsRover(start_point, direction)

        self.assertEqual(mars_rover.starting_coordinates(), (start_point, direction))

    #2. The rover receives a character array of commands.
    #2.1. Implement commands that turn the rover left/right (l,r).
    @parameterized.expand([
        (Compass.N,  Compass.E),
        (Compass.E,  Compass.S),
        (Compass.S,  Compass.W),
        (Compass.W,  Compass.N)
    ])
    def test03_turn_clockwise_starting_from_north(self, initial_facing, ends_facing):
        x = 0
        y = 0
        start_point = Point(x,y)
        direction = Compass.N
        mars_rover = MarsRover(start_point, initial_facing)
        mars_rover.turn(TurnCommands.RIGHT)
        self.assertEqual(mars_rover.facing(), ends_facing)

    #2.2. Implement commands that move the rover forward/backward (f,b).

    # parameterized should follow AAA from left to righ
    # (Arrange, Arrange, Act, Assert)
    @parameterized.expand([
        (Compass.S,  Point(0,0), MoveCommand.FORWARD, Point(0, 1)),
        (Compass.S,  Point(1,1), MoveCommand.BACKWARD, Point(1, 0)),
        (Compass.E,  Point(0,0), MoveCommand.FORWARD, Point(1, 0)),
        (Compass.E,  Point(1,1), MoveCommand.BACKWARD, Point(0, 1)),
    ])
    def test04_move_commands(self, initial_facing, initial_point, move_command, ends_position):
        mars_rover = MarsRover(initial_point, initial_facing)
        mars_rover.move(move_command)
         
        self.assertTrue(mars_rover.current_position() == ends_position)
    
    # parameterized should follow AAA from left to righ
    # (Arrange, Arrange, Act, Assert)
    @parameterized.expand([
        (Compass.W,  Point(0,0),  MoveCommand.FORWARD, OutOfWorldBoundariesError),
    ])
    def test05_move_commands_throw_exceptions(self, initial_facing, initial_point, move_command, expected_exception):
        mars_rover = MarsRover(initial_point, initial_facing)
        
        self.assertRaises(expected_exception, mars_rover.move, move_command)