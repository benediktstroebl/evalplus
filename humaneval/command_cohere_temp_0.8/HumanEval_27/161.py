```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns its letters in reversed case while keeping uppercase letters unchanged. For instance, if you use this function on the "hello" string, it will return "hELLO".

To run tests in Python, you can use the built-in `unittest` module. This module provides a set of testing tools and assertions that make it easy to organize and run tests. If you haven't already, you can install `unittest` via `pip` with the following command:
```bash
pip install unittest
```

For the given function, here's how you can implement a basic test suite using `unittest`:
```python
import unittest

def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c for c in string)

class TestFlipCase(unittest.TestCase):
    def test_flip_case(self):
        self.assertEqual(flip_case('HELLO'), 'hELLO')
        self.assertEqual(flip_case('hello'), 'hELLo')
        self.assertEqual(flip_case('fooBar'), 'fOObAR')
    
    def test_flip_case_empty_string(self):
        self.assertEqual(flip_case(''), '')
    
    def test_flip_case_mixed_case(self):
        self.assertEqual(flip_case('AhOO'), 'hAOO')

if __name__ == '__main__':
    unittest.main()
```

In the above code:
- `test_flip_case`: This test checks the functionality of the `flip_case` function for various input scenarios.
- `test_flip_case_empty_string`: This test evaluates the function's behavior when an empty string is passed.
- `test_flip_case_mixed_case`: This test assesses the function's ability to correctly flip the case for mixed-case strings. 

Each test is formulated using `unittest.TestCase` to harness the power of 'unittest' for creating and running tests. The `unittest.main()` function is necessary to initiate test execution.

To execute the test suite, open a terminal, navigate to the directory housing the script, and run the command:
```bash
python test_flip_case.py
```

If all tests pass, you'll get a reassuring output:
```python
....
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

If any test fails, the output will be accompanied by the specific assertion error, aiding you in identifying the areas that require your attention.