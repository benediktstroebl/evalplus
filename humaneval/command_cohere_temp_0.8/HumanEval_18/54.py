Here's a Python function that solves the problem of finding the number of times a substring occurs in a given string. The function takes two strings as input and returns the number of times the substring occurs in the string, including overlapping occurrences:
```python
def how_many_times(main_string, substring):
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    """
    if not main_string or not substring:
        return 0
    
    count = 0
    pos = 0
    
    while pos < len(main_string):
        temp_pos = main_string.find(substring, pos)
        if temp_pos == -1:
            break
        count += 1
        pos = temp_pos + 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This function uses the `find` method to search for the substring in the main string. The `find` method returns the first index where the substring is found, or -1 if it's not found. The function then increments the count if the substring is found and continues searching from the next position. The tests provided in the prompt will ensure the function works correctly. 

You can copy and paste this code into a Python environment or script to test it out.  If you'd like, we can execute these tests here in the chat as well, to ensure the correctness of this solution.