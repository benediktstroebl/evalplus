```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaa"

assert how_many_times(string1, string1) == 3
assert how_many_times(string2, string2) == 3
assert how_many_times(string3, string3) == 3
assert how_many_times("a", "a") == 2
assert how_many_times("aa", "a") == 3
```
This code defines a function how_many_times that takes two parameters: a string and a substring. It uses a basic loop to count the number of times the substring appears in the string. The function then returns the