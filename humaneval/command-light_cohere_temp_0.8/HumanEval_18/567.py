```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for char in substring if char in string)

# Test case 1: Check if function returns 0 when the substring is not present
test_1 = assert how_many_times('', 'a') == 0

# Test case 2: Check if function correctly counts occurrences
test_2 = assert how_many_times('aaaa', 'aa') == 3

# Test case 3: Verify correct handling of overlapping substrings
test_3 = assert how_many_times('aaa', 'aaa') == 3

print("All tests passed!")
```