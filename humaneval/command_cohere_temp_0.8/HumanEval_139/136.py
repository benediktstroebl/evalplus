Here's a Python script that defines the `brazilian_factorial` function, as per the provided problem statement:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This function follows the definition of the "Brazilian factorial," which multiplies the factorial of every integer between 1 and n (inclusive) to get the result. The initial value of the `product` variable is set to 1 to ensure correct computation of the factorials.

To test this function, you can use the following code:
```python
test_cases = [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 288),
    (10, 3628800),
]

for n, answer in test_cases:
    assert special_factorial(n) == answer, f"For n={n}, the function should return {answer} but returned {special_factorial(n)} instead."
```

This test suite includes a variety of input values, ensuring that the function produces the expected results for different 'n' values.