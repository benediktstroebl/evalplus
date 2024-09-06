```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer less than number from number, which is the basic definition of truncation. 

To test this function, you can call it with a float input and see if it returns the expected output:
```python
result = truncate_number(3.5)
print(result)  # Output: 0.5
``` 

Alternatively, you can check if the function returns the expected output using a built-in Python module, `testscenarios`. Here is an example of how to implement this script into a `testscenarios` module: 
```python
import testscenarios

def truncate_number(number: float) -> float:
    return number - int(number)

class TestTruncateNumber(testscenarios.TestCase):
    def test_truncate_number(self):
        result = truncate_number(3.5)
        self.assertEqual(result, 0.5)

    def test_truncate_negative_number(self):
        self.assertRaises(ValueError, truncate_number, -3.5)

if __name__ == '__main__':
    testscenarios.run_tests()
```

In the above code, the `testscenarios` module is used to define test cases for the `truncate_number` function. The `TestCase` class is inherited to define test cases. `test_truncate_number` checks if the result of truncating 3.5 is indeed 0.5, and `test_truncate_negative_number` checks if a ValueError is raised when trying to truncate a negative number.  The `run_tests()` function is called to execute the tests when the script is run directly. 

To run the script, save it in a file (e.g., `test_truncate_number.py`) and execute it in your Python environment. 

This way, the code will automatically run the tests and indicate whether they pass or not, providing confidence that the function behaves as expected.