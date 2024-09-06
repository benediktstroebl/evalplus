Here is a self-contained Python script with a function that solves the problem you described:
```python
def how_many_times(string, substring):
    return len(string.find(substring))

# Unit tests
test_how_many_times = {
    "a" : 0,
    "aaa" : 3,
    "aaaa" : 2,
}

for text, exp in test_how_many_times.items():
    actual = how_many_times(*text)
    assert actual == exp
```
This script defines a function `how_many_times` that takes a string and a substring as arguments, and returns the number of times the substring is found in the string. It also provides a test cases to verify the functionality of the function.