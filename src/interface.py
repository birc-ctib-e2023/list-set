"""Interface a set must implement."""

from typing import (
    Protocol, TypeVar, Iterable
)

T = TypeVar('T', contravariant=True)


class Set(Protocol[T]):
    """A set of elements of type T."""

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ...
