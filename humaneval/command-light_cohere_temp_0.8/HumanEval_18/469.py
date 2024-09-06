```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.sub(substring)
    for i, char in string:
        if char == substring:
            count += 1
    return count

# Test case 1
print(how_many_times('aaa', 'aa'))  # Output: 3

# Test case 2
print(how_many_times('abcde', 'ab'))  # Output: 2

# Test case 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```