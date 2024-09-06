```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "a"
string3 = "aaaa"
string4 = "aaaaaa"

for t in [string1, string2, string3, string4]:
    assert how_many_times(t, "a") == 3

for t in [string1, string2, string3, string4]:
    assert how_many_times(t, "aa") == 3

for t in [string1, string2, string3, string4]:
    assert how_many_times(t, "aaa") == 3

for t in [string1, string2, string3, string4]:
    assert how_many_times(t, "aaaa") == 3

for t in [string1, string2, string3, string4].upper():
    assert how_many_times(t, "AAA") == 6
```