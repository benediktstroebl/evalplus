### Summing Numbers from 1 to N

Here is a Python script that defines a function to sum numbers from 1 to `n`:

```markdown
### Code
```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    return sum(range(1, n + 1))
```

### Example Use Cases

```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

### Explanation

This script defines a function called `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the built-in `sum` function in combination with the `range` function to calculate the sum efficiently. The `range` function generates a sequence of numbers from 1 to `n`, and the `sum` function adds up these numbers. The `+ 1` in `range(1, n + 1)` is necessary to include the number `n` in the sum.

This script is self-contained, meaning it can be run as is without requiring any external dependencies. It defines the `sum_to_n` function and provides example use cases to demonstrate its usage.