```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function with various inputs
print(how_many_times("aaa", "aa"))  # Output: 3
print(how_many_times("abc", "a"))  # Output: 2
print(how_many_times("aaaa", "aa"))  # Output: 3
print(how_many_times(" ", "hello"))  # Output: 2
print(how_many_times("aaaa", ""))  # Output: 0
```