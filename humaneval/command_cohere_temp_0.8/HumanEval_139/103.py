Here's a Python script that defines the `brazilian_factorial` function as per the provided description:
```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```

This function definition is inline with the explanation provided, where `special_factorial` returns the regular factorial of n. It iterates through numbers from 1 to n, updating the `fact` variable to the product of all numbers, which is the regular factorial value.