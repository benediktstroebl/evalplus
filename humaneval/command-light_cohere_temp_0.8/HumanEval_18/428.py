```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

# Test the function
string = "aaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result) # Output: 6

# Test again
string = "abc"
substring = "a"
result = how_many_times(string, substring)
print(result) # Output: 3
```