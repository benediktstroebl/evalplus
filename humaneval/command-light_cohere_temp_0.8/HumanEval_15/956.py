Here's the self-contained Python script that defines and tests a function to generate a string of numbers starting from 0 up to the given limit n:
```python
import pytest
def test_string_sequence(test):
    n = 5
    expected = '0 1 2 3 4 5'
    result = test.string_sequence(n)
    assert result == expected
test_string_sequence(TestCase())
```
Do you have any further questions related to testing or debugging Python code?