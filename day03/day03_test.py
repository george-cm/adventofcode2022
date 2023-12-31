import pytest

from day03 import calculate_priority  # type: ignore  # noqa: E402
from day03 import solve_part1, solve_part2  # type: ignore # noqa: E402

INPUT_S: str = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def banner(msg: str) -> str:
    return f"\n{'=' * len(msg)}{msg}{'-' * len(msg)}"


def test_calculate_priority() -> None:
    assert calculate_priority("a") == 1
    assert calculate_priority("b") == 2
    assert calculate_priority("c") == 3
    assert calculate_priority("x") == 24
    assert calculate_priority("y") == 25
    assert calculate_priority("z") == 26
    assert calculate_priority("A") == 27
    assert calculate_priority("B") == 28
    assert calculate_priority("C") == 29
    assert calculate_priority("X") == 50
    assert calculate_priority("Y") == 51
    assert calculate_priority("Z") == 52


def test_sove_part1() -> None:
    assert solve_part1(INPUT_S) == 157


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 70


if __name__ == "__main__":
    pytest.main(["-vv", "-s"])
