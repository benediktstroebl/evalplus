```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    :param string: Input string
    :return: Number of distinct characters in the string
    """
    # Convert the string to lower case to make the comparison case-insensitive
    lower_string = string.lower()
    
    # Convert the string to a set, which automatically removes duplicate characters
    distinct_chars = set(lower_string)
    
    # Return the number of distinct characters
    return len(distinct_chars)


# Test cases
print(count_distinct_characters('xyzXYZ'))  # Expected output: 3
print(count_distinct_characters('Jerry'))   # Expected output: 5
print(count_distinct_characters('aaaa'))    # Expected output: 1
print(count_distinct_characters(''))        # Expected output: 0
```

Alternatively, you can use a one-liner solution:

```python
def count_distinct_characters(string: str) -> int:
    """
    Given a string, find out how many distinct characters (regardless of case) does it consist of

    :param string: Input string
    :return: Number of distinct characters in the string
    """
    return len(set(string.casefold()))
```