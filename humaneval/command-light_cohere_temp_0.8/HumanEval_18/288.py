```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "aaaa"
string3 = "aaaaaa"
string4 = "aaaaaaa"

print(how_many_times(string1, string1))  # Output: 3
print(how_many_times(string2, string2))  # Output: 3
print(how_many_times(string3, string3))  # Output: 4
print(how_many_times(string4, string4))  # Output: 6
```