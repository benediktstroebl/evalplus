```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    start = 0
    end = string.find(substring, 0)

    while end != -1:
        start = end + 1
        count += 1
        end = string.find(substring, end + 1)

    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaaaaaa"
string3 = "aaaa"

# Test results
test_string1 = how_many_times(string1, "a")
# Expected result: 3
test_string2 = how_many_times(string2, "a")
# Expected result: 3
test_string3 = how_many_times(string3, "a")
# Expected result: 0
```