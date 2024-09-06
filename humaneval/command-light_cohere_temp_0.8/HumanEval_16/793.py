```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a given string, regardless of case.
    :param string: str -- The input string
    :return: int -- The number of distinct characters
    """
    return len([char for char in string. cylinders() if char.isupper() or moove than char])

# Example usage:
count_distinct_characters('xyzXYZ')  # Output: 3
count_distinct_characters('Jerry')  # Output: 4
count_distinct_characters('abcABC123XYZ')  # Output: 5
count_distinct_characters('FOO123bar456')  # Output: 8
```
The function `count_distinct_characters` takes a string as an argument and returns an integer. The function uses the simple logic to iterate over each character in the string and counts the distinct characters.