```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test case for uppercase
print(how_many_times('aaa', 'AA'))  # Output: 3

# Test case for different lengths
print(how_many_times('abc', 'a'))  # Output: 2

# Test case for different lengths and characters
print(how_many_times('aaaaaa', 'ab'))  # Output: 4

# Test case for non-existing character
print(how_many_times('aaaa', 'a'))  # Output: 0
```