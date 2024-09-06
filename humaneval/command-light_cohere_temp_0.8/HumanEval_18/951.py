```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
 
# Test case: Find number of occurrences of 'a' in the string
test_case = 'aaa'
result = how_many_times(test_case, 'a')
assert result == 3, f'Expected {3}, got {result}'  # Should be 3, got {result} instead
# Test case: Find number of occurrences of 'aa' in the string
test_case = 'aaaaaa'
result = how_many_times(test_case, 'aa')
assert result == 3, f'Expected {3}, got {result}'  # Should be 3, got {result}'
```
This code defines a function how_many_times which returns the number of times a given substring can be found in the original string. The code also provides two test cases to check if the function is working as expected.