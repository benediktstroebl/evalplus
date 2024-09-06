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
    assert special_factorial(5) == 240120
```

This script defines a function `special_factorial` that calculates the 'Brazilian factorial' as defined in the problem statement. It iterates through all numbers from 1 to `n` and calculates the factorial, then iterates from 2 to n and aggregates the result by dividing it with the factorial of each number. The `factorial` function is also provided to calculate the factorial of a given number. Finally, the script includes a test case to validate the correctness of the `special_factorial` function.