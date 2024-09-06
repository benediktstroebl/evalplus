```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))

# test
test_case = """aaaaaa
ab
"""
print(how_many_times(test_case, 'a'))
```