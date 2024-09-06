Here's a self-contained Python function that finds the number of times a given substring can be found in the original string, while accounting for overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    :overlapping: Overlapping cases are allowed.
    Count string.
    :param string: The original string
    :param substring: The substring to find in the original string
    :return: Number of occurrences of the substring
    """
    return len(string.find(substring))
```

This function takes two parameters: a string and a substring, and returns the number of occurrences of the substring in the original string. It uses the Python's string.find() method to count the occurrences of the substring in the original string.

You can use this function with your own test cases to find the number of occurrences of any given substring.