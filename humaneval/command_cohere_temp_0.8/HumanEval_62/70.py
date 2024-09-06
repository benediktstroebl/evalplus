```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs """
    num_terms = len(xs) - 1
    derivative_coefficients = [0] * num_terms
    for i in range(num_terms):
        derivative_coefficients[i] = xs[i + 1] * (i + 1)
    return derivative_coefficients
```

The following test cases are included to ensure correctness:
```python
def test_derivative():
    # Test Case 1
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Test Case 2
    assert derivative([1, 2, 3]) == [2, 6]

    # Test Case 3
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]

test_derivative()
```

To run the test cases, you should install the pytest library, which is a popular testing library in Python. After installing it, you can run the test file using the following command:
```python
python -m pytest
``` 

This command will execute all the test cases in the test file named `test_derivative.py`. If all test cases pass without error, you will see an output similar to the following:
```
test_derivative.py  .........(...)

===================== 2 passed, 1 failed in 0.03 seconds ======================
``` 
If you prefer a quieter output, you can also add the `--quiet` flag, which will suppress most of the output. 

Please let me know if you would like to make any adjustments or add any additional details!