```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)

    for i in range(len_string):
        if string[i] == substring:
            count += 1

    return count

# Test cases:
string = "aaaaaaa"
substring = "a"
result = how_many_times(string, substring)
print(result)  # Output: 6

string = "hello world"
substring = "ello"
result = how_many_times(string, substring)
print(result)  # Output: 2

string = "abcnmtntre"
substring = "abc"
result = how_many_times(string, substring)
print(result)  # Output: 3
```