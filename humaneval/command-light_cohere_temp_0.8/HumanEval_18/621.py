```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_substring = len(substring)
    for i in range(len(string)):
        if string[i:i+length_substring] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
assert result1 == 3

string2 = "abc"
substring2 = "a"
result2 = how_many_times(string2, substring2)
assert result2 == 0

string3 = "abc"aaaa"
substring3 = "aa"
result3 = how_many_times(string3, substring3)
assert result3 == 3

```
This code defines a function how_many_times that calculates the frequency of a given substring within a given string. It iterates over the How many times a substring can be found in the original string by comparing character ranges. The test cases verify the basic scenarios, including different lengths of the substring and different positions in the original string.