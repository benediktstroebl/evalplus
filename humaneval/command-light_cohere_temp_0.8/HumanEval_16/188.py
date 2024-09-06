```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with a string that should pass
test_count_distinct_characters = """xy xZzzyz # this should give us 4 distinct characters
```
test_count_distinct_characters
assert count_distinct_characters("xy xZzz") == 4

# Test the function with a string that should fail (two instances of the same character)
test_count_distinct_characters = """Jerry JERRY" # this should give us 3 distinct characters

assert count_distinct_characters("Jerry JERRY") == 3  # this should fail
```