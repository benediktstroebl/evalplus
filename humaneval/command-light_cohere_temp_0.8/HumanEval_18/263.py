```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "a"
string3 = "aaaa"
string4 = "aa"

sub_string = "a"

result1 = how_many_times(string1, substring)
# Result: 4

result2 = how_many_times(string2, substring)
# Result: 2

result3 = how_many_times(string3, substring)
# Result: 3

result4 = how_many_times(string4, substring)
# Result: 1
```