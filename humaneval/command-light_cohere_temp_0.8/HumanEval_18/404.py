```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
assert result1 == 3

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
assert result2 == 2

string3 = "abc123"
substring3 = "abc"
result3 = how_many_times(string3, substring3)
assert result3 == 3

string4 = "hello world"
substring4 = "o"
result4 = how_many_times(string4, substring4)
assert result4 == 2
```
The above code defines the function `how_many_times` that finds the count of occurrences of a given substring in a given string. The function uses a simple loop and compares each character with the substring. 

Please note that the code is self-contained and does not require any additional imported functions or modules.