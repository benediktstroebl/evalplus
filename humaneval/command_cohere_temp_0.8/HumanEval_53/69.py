```python
def add(x: int, y: int):
    """
    Add two numbers x and y
    Returns:
        int: Sum of x and y
    """
    return x + y
```
The function adds two numbers passed as arguments and returns their sum. The specification states that the numbers are of integer type, so the integer type is assigned to the return type. 

To ensure the function adheres to the specified behavior, it is recommended to include tests that cover different cases. These tests can be integrated into the script using Python's `unittest` module. 

For example, you can add:
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero_to_number(self):
        self.assertEqual(add(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
```

This provides a basic testing framework to validate the `add` function and ensure its behavior aligns with the problem statement. Feel free to adjust the tests according to your specific requirements or to further verify the functionality of the `add` function. 
If you provide more details or additional requirements, I can further refine the code and tests to suit your needs.