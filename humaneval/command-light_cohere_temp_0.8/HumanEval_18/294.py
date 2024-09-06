Here's the Python code with the self-contained function `how_many_times`, which is designed to find the number of occurrences of a given substring within a given string, considering case and spacing:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    considering case and spacing.
    """

    def substring_count(s):
        count = 0
        for char in s:
            if char == substring:
                count += 1
        return count
    return substring_count(string.lower())
```
The function uses a helper function `substring_count` to count the occurrences of the substring. If you string is all lowercase, it converts both the substring and the original string to lowercase to make the comparison case-insensitive.