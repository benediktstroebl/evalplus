### Sum Numbers from 1 to N
```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))

# Example usage:
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
In this code, the `sum_to_n` function uses the built-in `sum` function along with the `range` function to generate numbers from 1 to `n` (inclusive) and then sums them up. The `range` function generates a sequence of numbers up to but not including the stop value, so we use `n + 1` as the stop value to include `n` in the sum.