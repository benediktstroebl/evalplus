```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string): 
            if char == substring)

# Test the function with various inputs
string1 = "aaa"
string2 = "a"
string3 = "aaaa"
string4 = ""

assert how_many_times(string1, "a") == 3
assert how_many_times(string2, " ") == 0
assert how_many_times(string3, "aaaa") == 3
assert how_many_times(string4, "aa") == 0
```