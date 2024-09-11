### Largest Divisor of a Number
#### Problem Description
Find the largest number that divides a given number `n` evenly, smaller than `n`.

#### Solution

```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Initialize the divisor as n-1
    divisor = n - 1

    # Iterate from n-1 down to 1
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the divisor
            divisor = i
            # We can break the loop since we're looking for the largest divisor
            break

    return divisor
```

#### Example Use Cases

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 8
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function uses a loop to iterate from `n-1` down to 1 and checks each number to see if it is a divisor of `n`. The first number that is a divisor is returned as the result.