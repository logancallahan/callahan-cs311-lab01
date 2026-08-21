"""
Lab 1: The Typed Script -- TypedContainer starter.

Complete TypedContainer below. See the assignment, Part B,
for the full requirements. Do not rename the class or its methods --
test_container.py imports them by name.
"""

from typing import Generic, TypeVar

T = TypeVar("T")


class TypedContainer(Generic[T]):
    """A strictly-typed key-value container. Keys must always be str."""

    def __init__(self) -> None:
        self._dictionary: dict[str, T] = {}

    def set(self, key: str, value: T) -> None:
        """
        Store `value` under `key`.

        Must raise TypeError immediately if `key` is not a str --
        no silent coercion. See Part A, Question 3, for why.
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        self._dictionary[key] = value
            

    def get(self, key: str) -> T:
        """
        Return the value stored under `key`.

        Must raise TypeError immediately if `key` is not a str.
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        return self._dictionary[key]

    def __contains__(self, key: str) -> bool:
        return key in self._dictionary

    def __len__(self) -> int:
        return len(self._dictionary)
