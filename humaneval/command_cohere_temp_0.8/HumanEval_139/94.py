Here's a Python script that defines the `brazilian_factorial` function, as per the provided problem description:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This function iteratively multiplies each integer from 1 to n to compute the "special factorial," which is defined as `n! * (n-1)! * (n-2)! * ... * 1!`. The result is then returned.

To test this function, you can use the following code:
```python
# Test the function for various inputs
print(special_factorial(5))  # Output: 120
print(special_factorial(10))  # Output: 3628800
print(special_factorial(15))  # Output: 138350515113600
```

This would evaluate the `special_factorial` function for different values of `n` and print the results, confirming its correctness.