import pytest

from day09 import solve_part1, solve_part2  # type: ignore  # noqa: E402 F401

INPUT_S: str = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S, visualize=False) == 13


def test_solve_part2_short() -> None:
    assert solve_part2(INPUT_S, visualize=True) == 1


def test_solve_part2_long() -> None:
    inputs = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    assert solve_part2(inputs, visualize=True) == 36


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
