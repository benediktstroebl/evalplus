Here's a Python script that defines the `brazilian_factorial` function as per the provided problem description:
```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```

This function iteratively multiplies each integer from 1 to n to compute the special factorial. It then returns the result.

To test this function, you can use the following code:
```python
Test special_factorial():
    # Test case 1:
    assert special_factorial(5) == 12024094700225920000
    # Test case 2:
    assert special_factorial(3) == 6
    # Test case 3:
    assert special_factorial(1) == 1
```

Assuming the correct script is saved in a file named `brazilian_factorial.py`, you can run the tests using the command `python brazilian_factorial.py` in your terminal. 

The three explicit tests cover different `n` inputs and ensure the function handles any edge cases. The `assert` statements will verify that the output of `special_factorial` matches the expected results. If the functions are correct, you should see the pass message from Python after executing the file.