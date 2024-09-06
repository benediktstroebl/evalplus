```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): Number of integers to sum

    Returns:
        int: The sum of the first n integers
    """
    return sum(range(1, n + 1))
```

This version of the code ensures that the sum_to_n function is self-contained and will work on its own without relying on external variables. It also includes a comment to explain the purpose of the function and provides intuition for how it works. 

This function can be called with various input values to ensure it works correctly:
```python
print(sum_to_n(30))  # Should output: 465
print(sum_to_n(100))  # Should output: 5050
print(sum_to_n(5))  # Should output: 15
print(sum_to_n(10))  # Should output: 55
print(sum_to_n(1))  # Should output: 1
```

The output would be:
```
465
5050
15
55
1
```