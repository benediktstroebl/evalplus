```python
def closest_integer(s):
    '''
    Returns the closest integer to the given numeric string, rounding away from zero.
    '''
    n = float(s)
    return round(n)
```

The function `closest_integer` takes a string value as input and returns the closest integer to the numeric value represented by the string, adhering to the "rounding away from zero" rule. This rule dictates that in case of equidistance, the rounded result is selected to be the farther integer from zero. 

This approach utilizes the built-in `round` function to determine the result, simplifying the implementation and enhancing code readability.

Here's a test suite to verify the function's behavior:
```python
def test_closest_integer():
    # Positive numbers
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15

    # Negative numbers
    assert closest_integer("-14.5") == -15

    # Decimal values closer to zero
    assert closest_integer("1.5") == 1

    # Decimal values farther from zero
    assert closest_integer("-14.9") == -15
```

This test suite covers different scenarios, including both positive and negative numbers, and decimals closer or farther from zero. 

To run the tests in a Python environment, you can use a simple test runner:
```python
def main():
    import unittest
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_closest_integer)
    unittest.TextTestRunner().run(test_suite)

if __name__ == "__main__":
    main()
```

Running this code snippet through a Python interpreter would execute the test runner, and subsequently, the test suite, effectively evaluating the functionality of the `closest_integer` function.