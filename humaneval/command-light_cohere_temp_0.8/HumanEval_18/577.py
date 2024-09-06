```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a substring in the original string.
    Overlapping cases are allowed
    """

    return sum(1 for char in string if char == substring)
    ```