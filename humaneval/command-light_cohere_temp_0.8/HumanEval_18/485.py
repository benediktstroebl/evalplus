```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    counting overlapping occurrences.
    Return: number of occurrences
    """

    # Split the input string on the substring
    words = [word for word in string if word == substring]

    # Count occurrences
    count = len(words)
    return count
```