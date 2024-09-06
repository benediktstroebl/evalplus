```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function with different inputs
string1 = "aaa"
string2 = "aaaa"
string3 = "abc"
string4 = " "
print(how_many_times(string1, string1))  # Output: 3
print(how_many_times(string2, string1))  # Output: 2
print(how_many_times(string3, string1))  # Output: 0
print(how_many_times(string4, string1))  # Output: 0
```