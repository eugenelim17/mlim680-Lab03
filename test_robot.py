import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_north_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_south_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST

def test_west_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST



def test_illegal_move(robot):
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_south(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_east(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1

def test_move_west(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_making_a_move(robot):
    robot.move()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 9
    assert state['col'] == 1

def test_back_track_after_making_a_turn(robot):
    robot.turn()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_making_multiple_move(robot):
    robot.move()
    robot.move()
    robot.move()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

def test_back_track_after_making_multiple_turn(robot):
    robot.turn()
    robot.turn()
    robot.turn()
    robot.back_track()
    robot.back_track()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1

