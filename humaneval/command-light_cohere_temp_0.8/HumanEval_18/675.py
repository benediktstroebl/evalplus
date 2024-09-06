Here is a Python script with a self-contained function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in string:
        if i == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "aaaa"aa"
string3 = "aaaa"aa"aa"

result1 = how_many_times(string1, "a")
result2 = how_many_times(string2, "aa")
result3 = how_many_times(string3, "aa")

assert result1 == 3
assert result2 == 3
assert result3 == 3
```

This code defines a function called how_many_times that takes a string and a substring as input. The function uses a loop to iterate over each character in the string. If the character matches the string, the count variable is incremented. The function then returns the count, which is the number of occurrences of the substring in the string.