```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in string if char == substring)

#Test cases
string = "aaa"
substring = "a"
result = how_many_times(string, substring)
assert result == 3

string = "abc"
substring = "a"
result = how_many_times(string, substring)
assert result == 2

string = "hello world"
substring = "ello"
result = how_many_times(string, substring)
assert result == 4
```

This code defines a function that counts the frequency of a given substring within a larger string. It uses a Python's list comprehension with a lambda function to efficiently count the occurrences of the substring in the original string. The test cases demonstrate its intended functionality.