```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns the count of occurrences of the substring in the string.
    Args: 
        string: The input string 
        substring: The substring to search for
    Returns: 
        count: Number of occurrences of the substring in the string
    """
    count = 0
    for char in substring:
        if string.find(char, 0) != -1:
            count += 1
    return count

# Testing the function
test_str = "aaaaaaa"
test_sub = "aa"
print(how_many_times(test_str, test_sub)) 
```