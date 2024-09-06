```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 10
    return (10 * starts_one_ends(n - 1) + 10) + (10 * starts_one_ends(n - 2) + 9)
```

This script provides a recursive solution to the problem. It takes into account that the first position is fixed (with a single 1), and the last position is fixed (with a single 1 and a following 9). Thus, it recursively solves for the numbers in the interior, subtracts 1 to account for the solved positions, and adds the counts for the starting and ending positions.

The function headers and some comments have been added to provide a more detailed explanation of the process. Also, this implementation uses a recursive approach, which is a typical solution for counting problems involving combinatorial patterns like this one. It is efficient in terms of time complexity, but keep in mind that it might lead to stack overflow for larger values of `n` due to its recursive nature. 

This approach can be optimized further using dynamic programming techniques, especially when handling larger input sizes, but this basic recursive approach is clear and concise. 

This approach can be optimized further using dynamic programming techniques, especially when handling larger input sizes, but this basic recursive approach is clear and concise.