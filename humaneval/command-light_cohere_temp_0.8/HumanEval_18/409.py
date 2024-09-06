```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "aa"
string3 = ""
substring1 = "a"
substring2 = "aa"
substring3 = "aaaa"

print("How many times for '" + string1 + "' and '" + substring1 + "' : " + how_many_times(string1, substring1))
print("How manytimes for '" + string2 + "' and '" + substring2 + "' : " + how_many_times(string2, substring2))
print("How manytimes for '" + string3 + "' and '" + substring3 + "' : " + how_many_times(string3, substring3))
print("How manytimes for '" + substring1 + "' and '" + substring2 + "' : " + how_many_times(substring1, substring2))
```