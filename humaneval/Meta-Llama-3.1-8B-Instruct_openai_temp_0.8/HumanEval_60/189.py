### Sum to N Function
#### Problem Description

This Python script defines a function `sum_to_n` that calculates the sum of numbers from 1 to a given number `n`.

#### Code

```markdown
# sum_to_n.py

def sum_to_n(n: int):
    """
    Calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.

    Examples:
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

# Test the function
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))  # Output: 15
    print(sum_to_n(10))  # Output: 55
    print(sum_to_n(1))  # Output: 1
```

#### Explanation

This script defines a function `sum_to_n` that uses the built-in `sum` function in combination with the `range` function to calculate the sum of numbers from 1 to `n`. The `range` function generates a sequence of numbers from 1 to `n` (exclusive), and the `sum` function adds up these numbers.

The script also includes a test section that demonstrates the function's behavior with different inputs.