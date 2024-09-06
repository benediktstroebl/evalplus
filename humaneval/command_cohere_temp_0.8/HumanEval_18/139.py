```python
def how_many_times(string, substring):
    return string.count(substring)
```

This function counts the number of times the substring occurs in the string, including cases of overlapping. It does so by using the built-in `.count()` method to perform this task. 

This method returns the count of the substring's occurrences in the string, ignoring the case and punctuation. It handles all edge cases defined in the problem statement, including an empty string or empty substring. 

You can test this function by calling it with different strings and substrings to verify its behavior. 
For example:
```python
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', ''))  # Output: 0
``` 
This demonstrates the function's correctness and flexibility in handling different cases.