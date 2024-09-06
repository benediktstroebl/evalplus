```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string = "aaaaaa"
substring = "aa"

result = how_many_times(string, substring)
assert result == 3

# Test cases 2: Check overlapping cases
string = "aaa"
substring = "a"

result = how_many_times(string, substring)
assert result == 0
```
The code defines a function that takes two parameters: a string and a substring. It then uses a loop to iterate over the string and count the number of occurrences of the substring. It returns the number of times the string contains the substring.