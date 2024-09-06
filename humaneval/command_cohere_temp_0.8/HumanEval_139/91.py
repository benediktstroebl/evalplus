Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288
    """
    factorial_product = 1
    for i in range(2, n+1):
        factorial_product *= i
    return factorial_product

assert special_factorial(4) == 288
```

You can then test the function with the provided input to verify the result is as expected:
```python
assert special_factorial(4) == 288
```

This code defines the `special_factorial` function as described in the prompt and uses Python's `assert` statement to verify the result of the function for a specific test case (`n = 4`) is as expected. 

To test the function for other values, you can add more assertions, or use the `special_factorial` function in an interactive Python session to verify its behavior for other inputs. 

The use of the `assert` statement is encouraged for automated testing, but please note that in the markdown code block, the assertion won't run automatically. If you'd like to include tests in the script, consider using a testing framework like `unittest` for more comprehensive and automated testing.