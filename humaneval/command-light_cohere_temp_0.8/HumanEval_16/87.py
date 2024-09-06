```python
def count_distinct_characters(string: str) -> int:
    """
    Returns the count of distinct characters in the given string, regardless of case.
    """
    character set from string is used to get all distinct characters, and set() is used to filter out duplicates
    """
    characters = character_set(string)
    return len(characters)

def character_set(string: str) -> set:
    """ Return a set of unique characters in the string """
    return set(string.lower())
```