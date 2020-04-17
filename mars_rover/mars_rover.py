from enum import Enum

class MarsRover:
    def __init__(self, current_position, direction):
        self._current_position = current_position
        self.direction = direction

    def starting_coordinates(self):
        return (self._current_position, self.direction)

    def turn(self, turn_command):
        self.direction = self._turn_switch(turn_command)

    def move(self, move_command):
        if self.check_boundaries(move_command):
            self._current_position = self._move_switch(move_command)
        else:
            raise OutOfWorldBoundariesError('Rover mars out of world limits')
    
    def facing(self):
        return self.direction

    def current_position(self):
        return self._current_position

    # -- PRIVATES --- #
    def check_boundaries(self, move_command):
        return {
            (Compass.N, MoveCommand.FORWARD):  self._current_position.y > 0,
            (Compass.N, MoveCommand.BACKWARD): self._current_position.y < 10,
            (Compass.S, MoveCommand.FORWARD):  self._current_position.y < 10,
            (Compass.S, MoveCommand.BACKWARD): self._current_position.y > 0,
            (Compass.E, MoveCommand.FORWARD):  self._current_position.x < 10,
            (Compass.E, MoveCommand.BACKWARD): self._current_position.x > 0,
            (Compass.W, MoveCommand.FORWARD):  self._current_position.x > 0,
            (Compass.W, MoveCommand.BACKWARD): self._current_position.x < 10
        }[(self.direction, move_command)]

    def _move_switch(self, move_command):
        return {
            (Compass.N, MoveCommand.FORWARD): Point(self._current_position.x, self._current_position.y - 1),
            (Compass.N, MoveCommand.BACKWARD): Point(self._current_position.x, self._current_position.y + 1),
            (Compass.S, MoveCommand.FORWARD): Point(self._current_position.x, self._current_position.y + 1),
            (Compass.S, MoveCommand.BACKWARD): Point(self._current_position.x, self._current_position.y - 1),
            (Compass.E, MoveCommand.FORWARD): Point(self._current_position.x + 1, self._current_position.y),
            (Compass.E, MoveCommand.BACKWARD): Point(self._current_position.x - 1, self._current_position.y),
            (Compass.W, MoveCommand.FORWARD): Point(self._current_position.x - 1, self._current_position.y),
            (Compass.W, MoveCommand.BACKWARD): Point(self._current_position.x + 1, self._current_position.y)
        }[(self.direction, move_command)]

    def _turn_switch(self, turn_command):
        return {
            (Compass.N, TurnCommands.RIGHT): Compass.E,
            (Compass.N, TurnCommands.LEFT): Compass.W,
            (Compass.E, TurnCommands.RIGHT): Compass.S,
            (Compass.E, TurnCommands.LEFT): Compass.N,
            (Compass.S, TurnCommands.RIGHT): Compass.W,
            (Compass.S, TurnCommands.LEFT): Compass.W,
            (Compass.W, TurnCommands.RIGHT): Compass.N,
            (Compass.W, TurnCommands.LEFT): Compass.S
        }[(self.direction, turn_command)]

class OutOfWorldBoundariesError(Exception):
    pass

class MoveCommand(Enum):
    FORWARD = 0
    BACKWARD = 1

class Compass(Enum):
    N = 0
    S = 1
    E = 2
    W = 3

class TurnCommands(Enum):
    LEFT = 0
    RIGHT = 1

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
          return '(x: {0}, y: {1}'.format(self.x, self.y)

    def __eq__(self, another_point):
        return self.x == another_point.x and self.y == another_point.y