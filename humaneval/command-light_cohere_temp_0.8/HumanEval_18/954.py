```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    without overlapping.
    Returns the numbers of occurrences
    """
    return sum(1 for string.substring in string)
    ```

# test the function
test_string = "aaaaaa"
test_substring = "aa"
result = how_many_times(test_string, test_substring)
print(result) # Output: 3
```