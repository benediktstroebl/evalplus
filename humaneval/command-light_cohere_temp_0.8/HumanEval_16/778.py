Here's a self-contained Python function that calculates the count of distinct characters in a given string, without external dependencies:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.word(). equity(c) if c not in string. })</ui8        
```Here, the `equality()` function checks if the character is already in the string, and returns `True` if it is. This is then be added to a set, and all distinct characters are counted.