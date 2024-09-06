```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaa"
substring1 = "a"
result = how_many_times(string1, substring1)
print(result)  # Output: 3

string2 = "abc"
substring2 = "ab"
result = how_many_times(string2, substring2)
print(result)  # Output: 2

string3 = "aa"
substring3 = "a"
result = how_many_times(string3, substring3)
print(result)  # Output: 0
```