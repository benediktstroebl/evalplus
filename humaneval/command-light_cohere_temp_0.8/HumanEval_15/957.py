Here's a self-contained Python function that returns a string containing space-delimited numbers starting from 0 up to the given number n:

```python
def string_sequence(n: int) -> str:
    return ' '.join([str(i) for i in range(n)])

# Test case 1:
test_suite = unittest.TestCase()
def test_string_sequence():
    assert str(string_sequence(0)) == '0'
    assert str(string_sequence(5)) == '0 1 2 3 4 5'

# Run the test case
test_suite.run()
```

This script defines a function that takes an integer n and returns a string containing the numbers from 0 to n, each separated by a space. It uses the list comprehension to generate the string and then tests if the function is working correctly.