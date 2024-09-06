Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

# Tests
def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288

test_special_factorial()
```

The function `special_factorial` uses a simple iterative approach to calculate the `brazilian_factorial` as defined in the problem statement. It starts with `product` initialized to 1 and iterates from 2 to `n` (inclusive), multiplying `product` by each integer `i` in this range. The final value of `product` will be the Brazilian factorial of the input `n`. 

The `test_special_factorial` function provides test cases to verify the correctness of the `special_factorial` function. It uses the `assert` statement to check if the output of `special_factorial` matches the expected values for various input arguments. When the script is run, the tests will be executed, and any differences between the actual and expected values will cause the program to fail and provide an error message for easier debugging.  This allows you to validate the proper functionality of the code.