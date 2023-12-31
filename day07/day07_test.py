import pytest

from day07 import solve_part1, solve_part2  # type: ignore  # noqa: E402

INPUT_S: str = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def test_solve_part1() -> None:
    assert solve_part1(INPUT_S) == 95437


def test_solve_part2() -> None:
    assert solve_part2(INPUT_S) == 24933642


if __name__ == "__main__":
    pytest.main(["-vv", "-s", __file__])
