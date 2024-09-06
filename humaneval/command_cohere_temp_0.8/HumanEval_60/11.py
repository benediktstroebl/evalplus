```python
def sum_to_n(n):
    """Returns the sum of the first n integers.
    
    Args:
        n (int): The highest number to be included in the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2  # Sum formula for first n natural numbers

# Testing the function with doctests
import unittest

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_with_positive_integers(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_with_negative_integers(self):
        self.assertEqual(sum_to_n(0), 0)
        self.assertEqual(sum_to_n(-5), 0)

    def test_sum_to_n_with_large_values(self):
        self.assertEqual(sum_to_n(1000), 500500)
        self.assertEqual(sum_to_n(10000), 5000500)

if __name__ == '__main__':
    unittest.main()
```

The provided Python script defines the function `sum_to_n`, which calculates the sum of the first 'n' integers as per the formula for the sum of the first 'n' natural numbers. It uses unittest to handle the tests, and the `TestSumToN` class contains test methods to validate the function's behavior with different input scenarios, including positive and negative integers and zero. 

If the script is run directly, the `unittest` framework automatically discovers and runs the test methods, generating feedback on whether the tests pass or fail. 

This way, you can concurrently test the function while comprehending its utilization through the provided tests. 

This approach adheres to Python's philosophy of "Batteries Included," where the language and its standard library prioritize comprehensive testing capabilities and solutions.