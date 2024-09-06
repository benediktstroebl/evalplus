```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count all occurrences of a given substring in the original string.
    'aaa' -> 3
    'aaaa' -> 3
    """
    return len([char for char in substring if char in string])

# Test cases
string1 = "aaa"
string2 = "aaaaaa"
string3 = "hello world"

result1 = how_many_times(string1, "a")
print(result1)  # Output: 3

result2 = how_many_times(string2, "aaaa")
print(result2)  # Output: 3

result3 = how_many_times(string3, "hello")
print(result3)  # Output: 0
```