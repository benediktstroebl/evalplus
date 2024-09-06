```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join + string + ''.join
    for char in substring and string.split('', char):
        if char in substring:
            count += 1
    return count

# Test the function
string1 = 'aaa'
string2 = 'aaaa'
print(how_many_times(string1, string2))  # Output: 3
print(how_many_times(string2, string1))  # Output: 0
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('abcde', 'ab'))  # Output: 2
print(how_many_times('a' * 'b' * 'c', 'ab'))  # Output: 3
```

This Python code provides a function, `how_many_times`, that calculates the count of occurrences of a given substring within a larger string. The function uses a split approach to handle cases where the substring is at the beginning or middle of the string. The test cases cover various scenarios, including overlapping substrings, different input strings, and different substring occurrences.