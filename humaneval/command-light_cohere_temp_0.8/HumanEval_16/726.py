```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c not c.lower()})
 distinct character counter in lowercase
def test_count_distinct_characters(test_string: str) -> None:
    assert count_distinct_characters(test_string) == len({c for c in test_string if c not c.lower()}), \
        out, the test passes. 
```  The `count_distinct_characters` function calculates the count of distinct characters in a given string, regardless of case. The `test_count_distinct_characters` function is a test function that checks the `count_distinct_characters` function's correctness with a test string. 
The function uses a dictionary comprehension and the `lower()` method to create a set of distinct characters in the string, and then uses the `len()` function to get the length of the set. 
Finally, the function returns `None` to indicate that the test passed successfully.