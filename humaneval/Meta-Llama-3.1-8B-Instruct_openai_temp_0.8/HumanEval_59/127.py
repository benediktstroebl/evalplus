Here's a Python script that solves the problem:
```markdown
## Largest Prime Factor Function

### Description
This script defines a function `largest_prime_factor(n)` that returns the largest prime factor of a given integer `n`. The function assumes that `n` is greater than 1 and is not a prime number.

### Code
```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Iterate from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = i
            # Divide n by i
            n = n // i
    
    # If n is not 1, it is the largest prime factor
    if n > 1:
        largest_factor = n
    
    return largest_factor

# Example use cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
### Explanation
The function uses a loop to iterate from 2 to the square root of `n`. In each iteration, it checks if the current number `i` is a factor of `n` by using the modulus operator (`n % i == 0`). If `i` is a factor, the function updates the largest factor and divides `n` by `i`. This process continues until `n` is reduced to 1, at which point the largest prime factor is returned. If `n` is not 1, it means that `n` itself is the largest prime factor, and the function returns `n`.

### Note
This function has a time complexity of O(sqrt(n)) and a space complexity of O(1), making it efficient for large inputs. However, please note that this implementation assumes that the input `n` is an integer greater than 1 and is not a prime number.