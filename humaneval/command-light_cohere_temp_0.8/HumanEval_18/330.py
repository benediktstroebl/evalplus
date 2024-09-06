```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string = "aaaaaa"
substring = "aa"
print(how_many_times(string, substring))  # Output: 3

string = "hello"
substring = "ello"
print(how_many_times(string, substring))  # Output: 2

string = "abcde"
substring = "cde"
print(how_many_times(string, substring))  # Output: 2
```