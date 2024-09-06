```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.def(ord) if c != ''})

# Test cases
test_pass = [('xyzXYZ', 3), ('Jerry', 4)]
test_fail = [('abcXYZ', 3), ('ABC', 1)]

# Test execution using pytest
pytest.run()
test_pass
assert count_distinct_characters(*test_pass) == test_pass[0][1], 'Distinct characters failed'

test_fail
assert count_distinct_characters(*test_fail) == test_fail[0][1], 'Distinct characters failed'
``` 
This code defines a function **`count_distinct_characters`** that calculates the count of distinct characters in a given string. It uses the straightforward character counting with Python's **`ord`** function to only consider non-blank characters and thereby disregard case. 

The test cases ensure the function's correctness by providing strings and expected distinct character counts. The `pytest` module is used for automated test execution, which provides a structured and efficient way to write test code.