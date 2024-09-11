### Greatest Common Divisor using Euclid's Algorithm
#### Python Script

```markdown
## greatest_common_divisor.py

### Function to calculate the Greatest Common Divisor (GCD) of two integers
### using Euclid's Algorithm.

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Return a greatest common divisor of two integers a and b
    
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    int: The greatest common divisor of a and b.
    """
    
    # Handle edge cases where b is zero
    if b == 0:
        return a
    
    # Use Euclid's algorithm to find GCD
    return greatest_common_divisor(b, a % b)


### Example Usage:

if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5

```

### How it works:

1. The function `greatest_common_divisor(a, b)` calculates GCD using Euclid's algorithm.
2. If `b` is zero, the function returns `a` as the GCD.
3. Otherwise, the function recursively calls itself with `b` and the remainder of `a` divided by `b` until `b` becomes zero.

### Time Complexity:

The time complexity of this algorithm is O(log min(a, b)), making it efficient for large integers.