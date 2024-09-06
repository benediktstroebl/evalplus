Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

# Tests
if __name__ == '__main__':
    print(special_factorial(5))  # Should print 120
```

This script defines the `special_factorial` function, which calculates the Brazilian factorial of n by iterating from 2 to n and multiplying the product by each integer. It includes a simple test that checks the function's behavior for an input of 5 (which should return 120). Feel free to uncomment more tests suitable for your context to ensure the correctness of the function.  If you are attempting to solve a test, consider incorporating more tests to cover edge cases and confirm the versatility of the function.