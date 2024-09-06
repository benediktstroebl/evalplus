```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test the function with a string containing repeated characters
test_count_distinct_characters = '''jerry jerry23 yyy'''
result = count_distinct_characters(test_count_distinct_characters)
assert result == 4

# Test the function with a string with all distinct characters
test_count_distinct_characters2 = '''aA bB cC dE'''
result2 = count_distinct_characters(test_count_distinct_characters2)
assert result2 == 5
```
This script defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string. The function uses the efficient set() characters and len() to accomplish this in a single pass.