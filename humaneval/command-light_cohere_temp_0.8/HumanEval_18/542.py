```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for c in string.string(substring) > 0)

# Test cases
string1 = "aaaaaaa"
string2 = "aaaa"
string3 = "aaa"
string4 = "aa"

print(how_many_times(string1, string1))
print(how_many_times(string2, string2))
print(how_many_times(string3, string3))
print(how_many_times(string4, string4))
```
The function counts the occurrences of the substring and returns the result.