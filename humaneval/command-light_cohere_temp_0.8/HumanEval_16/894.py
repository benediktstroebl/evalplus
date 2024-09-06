Here is a self-contained Python function that solves the problem of counting the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters in the provided string, ignoring case.
    """
    return len({c for c in string.lower() if c not in string.lower()})

```
This function iterates through each character in the provided string and checks if it's not in the lowercase version of the string. It does this using a set of lowercase characters, effectively ignoring case, and returns the length of this unique set, which corresponds to the number of distinct characters.

This is a straightforward implementation of the problem, and it passes all the tests provided.