```python
def add(x: int, y: int):
    return x + y
```
```
Tested against the provided Markdown test blocks, this function correctly adds two numbers.
```

The tests in the markdown file are not actual tests using Python's `unittest` framework or any other testing library. They are just pseudo tests that return values with the `>>>` marker, which are not real assertions. 

If you want to add proper test coverage using the `unittest` framework, you can add a test file with the `.py` extension that includes test functions declaring the specific assertions. Here is an example:
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    def test_add_zero_to_number(self):
        result = add(5, 0)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
```

In this example, we have a test class `TestAddFunction` that declares three test functions that cover different cases of adding two numbers. Each test function asserts that the result of the `add()` function is as expected using `self.assertEqual()`. 

To run the tests, you need to execute the test file directly or include the test file in a `test_` folder and run it using `pytest`. 

This way, you can have proper test coverage and ensure the function behaves correctly for various scenarios.