```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of times the substring can be find within the string without overlapping.
    """
    original string.
    count = 0
    string.find(substring, string) 
    while not string.isalpha(substring): 
        count += 1
    return count
    """

# Test case 1
print(how_many_times('', 'a')) # Output: 0

# Test case 2
print(how_many_times('aaa', 'a')) # Output: 3

# Test case 3
print(how_many_times('aaaa', 'aa')) # Output: 3
```

This function uses the `find()` function to locate the substring, and as long as the substring isn't found in the string, the function will increment the counter. 
Finally, it returns the total count of occurrences of the substring in the original string.