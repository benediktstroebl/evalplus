```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_ss = len(substring)
    for i in range(len(string)):
        if string[i:i+length_ss] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "a"
string4 = "aa"
string5 = "//////////"

result1 = how_many_times(string1, "aa")
result2 = how_many_times(string2, "a")
result3 = how_many_times(string3, "aaa")
result4 = how_many_times(string4, "a")
result5 = how_many_times(string5, "aaaa")

assert result1 == 3
assert result2 == 0
assert result3 == 3
assert result4 == 1
assert result5 == 3
```
The function **`how_many_times`** uses a simple method to count how many times a given substring can be found in the original string.  It uses a simple iteration to compare substrings, and it keeps track of the number of matches in a counter. For the function to be able to provide accurate results, it's essential to handle edge cases like empty strings and strings with only a certain substring.