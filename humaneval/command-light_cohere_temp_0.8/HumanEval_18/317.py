```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string) if char == substring)
    
# tests
test_str = "aaaaaa"
test_sub = "aa"
test_result = how_many_times(test_str, test_sub)
print("Test string:", test_str)
print("Test sub:", test_sub)
print("Test result:", test_result)
```