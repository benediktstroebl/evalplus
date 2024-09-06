```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "aaaa"
string3 = "aaaaaa"
string4 = "aaaaaaa"

print(how_many_times(string1, "a"))    # Output: 3
print(how_many_times(string2, "aa"))  # Output: 2
print(how_many_times(string3, "aaaa"))  # Output: 1
print(how_many_times(string4, "aaaa"))  # Output: 0
```