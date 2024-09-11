### Sum of Numbers from 1 to n
#### Problem Statement
The goal is to write a Python function that calculates the sum of numbers from 1 to `n`.

#### Solution
```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of numbers from 1 to n.

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
    return n * (n + 1) // 2
```
#### Explanation
This function uses the mathematical formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`. This formula is more efficient than iterating over the numbers from 1 to `n`, especially for large values of `n`.

#### Example Use Cases
```python
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```
This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula for the sum of an arithmetic series, which makes it efficient for large values of `n`. The script also includes example use cases to demonstrate how to use the function.