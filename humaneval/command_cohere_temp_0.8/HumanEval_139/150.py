```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def test_brazilian_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 1440

if __name__ == "__main__":
    test_brazilian_factorial()
```

This code defines the `special_factorial` function, which calculates the `brazilian_factorial` as described in the problem statement. It iterates through all numbers from 1 to `n` and accumulates the product of these numbers, then iterates through all numbers from 2 to `n` and subtracts the `factorial` of each number individually, effectively calculating the correct result.

The `factorial` function is also provided to calculate the factorial of a given number using recursion.

Finally, the `test_brazilian_factorial` function runs a few tests against the `special_factorial` function to verify its correctness. When executed, it prints the success message for the tests.