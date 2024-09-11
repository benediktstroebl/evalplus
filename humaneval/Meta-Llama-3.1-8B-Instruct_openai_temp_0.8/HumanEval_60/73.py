```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Example:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    return sum(range(1, n + 1))

# Test cases
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

However, since you asked for a scripted solution, here's how you can create a Python function using recursion to calculate the sum of numbers from 1 to n:

```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n using recursion.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.

    Example:
        >>> sum_to_n(30)
        465
        >>> sum_to_n(100)
        5050
        >>> sum_to_n(5)
        15
        >>> sum_to_n(10)
        55
        >>> sum_to_n(1)
        1
    """
    if n <= 1:
        return n
    else:
        return n + sum_to_n(n - 1)

# Test cases
print(sum_to_n(30))  # 465
print(sum_to_n(100))  # 5050
print(sum_to_n(5))  # 15
print(sum_to_n(10))  # 55
print(sum_to_n(1))  # 1
```

This recursive function works by adding the current number `n` to the sum of numbers from 1 to `n-1`. It base case is when `n` is less than or equal to 1, in which case it simply returns `n`. Otherwise, it calls itself with `n-1` as the argument and adds `n` to the result.