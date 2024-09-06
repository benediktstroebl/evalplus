import unittest
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)