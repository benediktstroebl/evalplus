```python
def special_factorial(n):
    """Returns the Brazilian factorial of integer n.

    Brazilian factorial is defined as:
    special_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!

    Parameters:
        n (int): Positive integer for which to calculate the special factorial.

    Returns:
        int: The special factorial of the input integer.
    """
    if n <= 0:
        return 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
```