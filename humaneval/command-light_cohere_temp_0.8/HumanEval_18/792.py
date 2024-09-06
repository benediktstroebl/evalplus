```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
assert result1 == 3

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
assert result2 == 3

string3 = "abc"
substring3 = "bc"
result3 = how_many_times(string3, substring3)
assert result3 == 2

string4 = "Hello World"
substring4 = "World"
result4 = how_many_times(string4, substring4)
assert result4 == 3

```
This Python code defines a function called `how_many_times` that takes two arguments: a string and a substring. It uses a variable `count` to count the number of occurrences of the substring in the string. The function returns the process by iterating over each character in the string and checking if it's equal to the substring. It then returns the result, which is the count of the occurrences.