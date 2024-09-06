```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of truncation. 

To test this function, you can call it with a float input and see if it returns the expected output:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 
Or you can check whether the function returns the expected value for other inputs, like:
```python
truncate_number(1.5)  # Expected output: 0.5
truncate_number(2.5)  # Expected output: 0.5
truncate_number(10.2)  # Expected output: 0.2
```
To do so, you can employ Python's built-in `unittest` module, which provides a simple framework for writing and running tests. 

Here is how you can implement those tests:
```python
import unittest

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_positive_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_positive_numbers(self):
        self.assertEqual(truncate_number(1.5), 0.5)
        self.assertEqual(truncate_number(2.5), 0.5)
        self.assertEqual(truncate_number(10.2), 0.2)

    def test_truncate_negative_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-3.5)

    def test_truncate_non_numeric_string(self):
        with self.assertRaises(ValueError):
            truncate_number('abc')

if __name__ == '__main__':
    unittest.main()
```
In this code, the `unittest` module is imported, and a test class `TestTruncateNumber` is defined, with several test methods. Each method tests a specific condition, and `assertEqual` is used to compare the expected output with the actual output of the `truncate_number` function. In the `if __name__ == '__main__'` block, `unittest.main()` is called to run all the defined test methods. 

To run this test suite, you can simply run the Python script in your terminal or command prompt, and the test results will be displayed, including the number of tests passed. 

Please note that this code considers the expectation that the input number is a positive float, and that the `truncate_number` function returns the decimal part of the number. If you have a different expectation for the function's behavior, you should adjust the test cases accordingly.