```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, taking overlapping occurrences into account.
    """

    using the dimapset-like matching to find all occurrences.
    Example string must contain the won't be considered a valid string
    """
    if not isinstance(string, str) or not string:
        raise TypeError("Input string must be a non-empty string")

    if not isinstance(substring, str) or not substring:
        raise TypeError("Input substring must be a non-empty string")

    if len(substring) > len(string):
        raise ValueError("The length of the substring is greater than the length of the string")

    return sum(1 for _ in string.posub.find(substring, return - string, 0))
```