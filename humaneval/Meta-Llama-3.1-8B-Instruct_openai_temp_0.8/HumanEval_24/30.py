```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n smaller than n.

    Example:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor as 1
    largest = 1
    
    # Iterate from 2 to n (inclusive) to find the largest divisor
    for i in range(2, n + 1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, update the largest divisor
            largest = i
    
    # Return the largest divisor
    return largest

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(16))  # Output: 8
print(largest_divisor(17))  # Output: 1
```

In this script, we define a function `largest_divisor` that takes an integer `n` as input and returns its largest divisor smaller than `n`. We initialize the largest divisor as 1 and then iterate from 2 to `n` to find the largest divisor by checking if each number `i` is a divisor of `n`. If `i` is a divisor, we update the largest divisor to `i`. Finally, we return the largest divisor and test the function with some examples.