```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.

    # Split substring and find the expected in the string
    if substring not in string:
        raise ValueError("Given substring is not in the string")

    # Return the count of occurrences of substring in the string
    return string.find(substring) + 1
```