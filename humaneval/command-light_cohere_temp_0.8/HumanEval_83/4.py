```python
def starts_one_ends(n):
    """
    Returns the count of 1-digit positive integers within n-digit numbers.
    ```
   
    function accepts positive integer n and returns the count of numbers >= 1 ending with 1 or starting with 1.
    """
"""
    # Count numbers that start or end with 1
    return sum([1 for x in range(1, n+1)] & [n for x in range(2, n+1)])

# Unit tests
def test_starts_one_ends():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(5) == 2
    assert starts_one_ends(7) == 2
    assert starts_one_ends(10) == 3
    assert starts_one_ends(12) == 4
    assert starts_one_ends(21) == 5
    assert starts_one_ends(1000) == 7
    assert starts_one_ends(9000) == 8

# Example usage
test_starts_one_ends()
```
This script defines a function `starts_one_ends` that calculates the count of positive numbers that start or end with 1 within a given range of numbers. It returns the the positive integer `n`, and returns the count of numbers greater than or equal to 1 that either start with 1 or end with 1. The script also provides unit tests for this function to ensure its correctness. 

Additionally, the function has an example usage where the count of numbers is demonstrated for different input ranges.