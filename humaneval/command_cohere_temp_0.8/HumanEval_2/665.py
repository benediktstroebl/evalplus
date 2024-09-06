```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than number from number, which inherently includes the integer part of the decomposition. The residual will be a float that is inherently less than 1, representing the desired decimal part of the decomposition. 

To test this, try calling the function with the example provided in the prompt:
```python
truncate_number(3.5)  # Returns 0.5
```
This is consistent with the example provided in the prompt. 

To expand the testing of this function, a set of unit tests could be added to ensure that the function behaves as expected for a variety of different inputs. Here is an example: 
```python
import unittest

def truncate_number(number: float) -> float:
    return number - int(number)

class TestTruncateNumber(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(truncate_number(1.5), 0.5)
        self.assertEqual(truncate_number(2.5), 0.5)
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_zero_to_one(self):
        self.assertEqual(truncate_number(0.1), 0.0)
        self.assertEqual(truncate_number(0.5), 0.0)
        self.assertEqual(truncate_number(0.99), 0.0)

    def test_integers(self):
        self.assertEqual(truncate_number(3), 0)
        self.assertEqual(truncate_number(10), 0)
        self.assertEqual(truncate_number(100), 0)

    def test_negative_numbers(self):
        self.assertEqual(truncate_number(-1.5), -0.5)
        self.assertEqual(truncate_number(-2.5), -0.5)
        self.assertEqual(truncate_number(-3.5), -0.5)

if __name__ == '__main__':
    unittest.main()
``` 

This will run the test suite with the new function and verify that it behaves as expected for a variety of different inputs.