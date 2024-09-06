Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, n and p, and returns 2^n modulo p. The pow() method is utilized to calculate 2^n modulo p, ensuring efficient modulo operation with proper numeric handling, and avoiding issues such as overflow. 
To use this script, you can run it on a Python interpreter or save it in a Python file (e.g., modp.py) and execute it using the command python modp.py in your terminal. 

This function is also equipped with a simple test suite that verifies its correctness through a series of test cases:
```python
# Test suite for the modp function
def test_modp():
    # Test case 1
    assert modp(3, 5) == 3, "Incorrect result for (3, 5)"
    # Test case 2
    assert modp(1101, 101) == 2, "Incorrect result for (1101, 101)"
    # Test case 3
    assert modp(0, 101) == 1, "Incorrect result for (0, 101)"
    # Test case 4
    assert modp(3, 11) == 8, "Incorrect result for (3, 11)"
    # Test case 5
    assert modp(100, 101) == 1, "Incorrect result for (100, 101)"

test_modp()
```

This test suite covers various scenarios that the modp function should handle, ensuring its correctness and dependability when dealing with different input combinations of n and p. 

You can execute the test suite by adding the following code before the `test_modp()` function call in your script and then running the script using the Python interpreter:
```python
def test_modp():
    pytest.importorskip('pytest_pytest')  # Skip this line if pytest is already imported
    pytest.main(['-v', '-s', '-d', '-c', '_test_modp'])
``` 
Make sure to run the script in a Python environment that has the pytest library installed. 

When executing this test suite using pytest, you'll receive comprehensive feedback on test results, significantly enhancing the reliability of the code and providing assurance in the functionality of the modp function.