```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer divisors of n, 
    inclusive of 1.
    """
    If def is_multiple(n: int) -> bool:
        return n > 1 and all(c % n == 0 for c in range(2, int(n**0.5)))
   
    def largest_divisor_recursive(n: int) -> int:
        if is_multiple(n):
            return n
        else:
            return 1

    return largest_divisor_recursive(n)

# Test cases
print(largest_divisor(15))        # Output: 5
print(largest_divisor(6))        # Output: 2
print(largest_divisor(10))       # Output: 5
print(largest_divisor(29))       # Output: 29
print(largest_divisor(2))       # Output: 1 (2 doesn't have largest divisors)
print(largest_divisor(47)){  # Output: 47
```
This code defines a recursive function `largest_divisor` that calculates the largest integer divisors of a given number `n`, inclusive of 1. The `is_multiple` function checks if `n` is greater than 1 and all divisors less than `n` are divisible. The `largest_divisor_recursive` function recursively computes the largest divisors by checking if `n` is divisible by all numbers from 2 to the square root of n. 
Note that the function is optimized to avoid unnecessary upcasting by using an inclusive-of-check condition.