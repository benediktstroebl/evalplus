```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    considering overlapping matches.
    Example the string: str, substring: str 
    Returns: int, the number of occurrences
    """
    return sum(1 for i, j in zip(string, substring))

# Test the function
test_how_many_times = how_many_times 
test_how_many_times('aaaa', 'aa') # Should return 3
test_how_many_times('abc', 'ab') # Should return 2
test_how_many_times('abc', 'a') # Should return 1
``` 
This code defines a function how_many_times that calculates the frequency of a given substring within a string. It returns the how many times the has been matched, which is the sum of the count of iterated indices i, j in the corresponding substrings in the original string.