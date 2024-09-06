```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    for i in range(1, length_string + 1):
        if string[i - 1 : i] == substring:
            count += 1

    return count

# Test the function
string = "aaaaaa"a"
substring = "a"
result = how_many_times(string, substring)
print(result)

# Test the function with overlapping substring
string = "aaaa"aaaa"a"
substring = "aa"
result = how_many_times(string, substring)
print(result)
```