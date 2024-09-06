```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaa"
string4 = "hello"
string5 = "World!"

tests = [
    ("Overlapping", "aa", "aaaaaa"),
    ("Non-overlapping", "a", "aaaa"),
    ("Overlapping with different case", "Hello", "aaaa"),
    ("Long text and short substring", string1, string3),
    ("Different cases", string4, "hello"),
    ("Long text and substring", string5, string1),
    ]

for case, sub, expected in tests:
    actual = how_many_times(case, sub)
    print(f"Case: {case}, {sub}, {expected}, actual: {actual}")
```