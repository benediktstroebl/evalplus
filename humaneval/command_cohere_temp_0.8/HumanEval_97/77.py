```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code works by breaking down the two input digits into their respective units using the modulo operator (`%`). It then multiplies these unit digits and handles any potential overflow (i.e., if the product is greater than 9) by taking the modular sum (`% 10`) to ensure the result remains in the range of 0 to 9.

To test this script, you can create a corresponding test file with the following content:
```python
# test_multiply.py

import unittest
from calculate_product import multiply

class TestMultiply(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(multiply(148, 412), 16)

    def test_example_2(self):
        self.assertEqual(multiply(19, 28), 72)

    def test_example_3(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_example_4(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_edge_cases(self):
        self.assertEqual(multiply(10, 5), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(9, 8), 72)

if __name__ == '__main__':
    unittest.main()
```

The script includes a variety of tests, including edge cases, to ensure the accuracy and robustness of the `multiply` function. By running this test file, you can verify that the function behaves as expected.