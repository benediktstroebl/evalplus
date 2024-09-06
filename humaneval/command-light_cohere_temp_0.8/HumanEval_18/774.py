```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = string.replace(substring) 
    while substring in string:
        count += 1
    return count

# Test cases
test_str = "aaaaaa"
test_sub = "a"
test_cases = [(test_str, test_sub)] * 3

for string, sub in test_cases:
    result = how_many_times(string, sub)
    assert result == 3
```