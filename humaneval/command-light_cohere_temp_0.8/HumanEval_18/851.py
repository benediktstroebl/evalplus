```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Test cases
string1 = "aaaaaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
print("Result1:", result1)

string2 = "aa"
substring2 = "aa"
result2 = how_many_times(string2, substring2)
print("Result2:", result2)

string3 = "hello"
substring3 = "lo"
result3 = how_many_times(string3, substring3)
print("Result3:", result3)
```

The code defines a function `how_many_times` that takes two arguments: a string and a substring. The function then iterates through the string and checks if the substring can be found by slicing. The function returns the number of times the substring is found.