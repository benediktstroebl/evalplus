```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test cases
string1 = "aaa"
string2 = "aaaaaa"
string3 = "aaaaaaa"

# Results: 3, 1, 1
print("Results:", [how_many_times(string1, 'a'), how_many_times(string2, 'a'), how_many_times(string3, 'a')]

```