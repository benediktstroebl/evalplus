Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    """
    Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288
    """
    factorial_list = [1]
    for i in range(2, n + 1):
        factorial_list.append(i * factorial_list[i-1])
    return factorial_list[n]

# Tests
def test_special_factorial():
    assert special_factorial(0) == 1
    assert special_factorial(1) == 1
    assert special_factorial(2) == 2
    assert special_factorial(3) == 6
    assert special_factorial(4) == 288
    assert special_factorial(5) == 2450

if __name__ == "__main__":
    test_special_factorial()
```

This code defines the `special_factorial` function using an iterative approach to calculate the Brazilian factorial. It also includes a simple test suite to verify the correctness of the function for different input values.