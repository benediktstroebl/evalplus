```python
def count_distinct_characters(string: str) -> int:
    return len(string)

# Test the function with various inputs
test_count_distinct_characters = """
def test_distinct_characters(string):
    assert count_distinct_characters(string) == len(string)
"""
test_distinct_characters('abc')  # Should return 3
test_distinct_characters('ABC')  # Should return 4
test_distinct_characters('jerry')  # Should return 4
```