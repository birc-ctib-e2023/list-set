"""Testing set implementations."""

from typing import Callable, Iterable
from interface import Set
from listset import ListSet, T

Cons = Callable[[Iterable[T]], Set[T]]


def check_set(set_type: Cons) -> None:
    """Test that we have an implementation of a set."""
    x = list(range(10))
    s = set_type(x)
    assert s

    for a in x:
        assert a in s
        s.remove(a)
        assert a not in s

    assert not s

    for a in x:
        s.add(a)
    for a in x:
        assert a in s
        s.remove(a)
        assert a not in s


def test_builtin() -> None:
    """Test builtin set."""
    check_set(set)


def test_list_set() -> None:
    """Test builtin set."""
    check_set(ListSet)
