### Largest Prime Factor
#### Python Script
```markdown
# Define a helper function to check if a number is prime
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Define the main function to find the largest prime factor
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Initialize the largest factor to 1
    largest_factor = 1
    
    # Check all numbers from 2 to n (inclusive) to find the largest factor
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if is_prime(i):
                # Update the largest factor if i is larger
                largest_factor = max(largest_factor, i)
    
    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

### Explanation

The `is_prime` function checks if a number is prime by dividing it by all numbers up to its square root. If it has any divisors, it's not prime.

The `largest_prime_factor` function iterates over all numbers from 2 to `n`, checking if each number is a factor of `n`. If it is, and it's prime, it updates the largest factor. The function returns the largest factor found.

Note that this solution has a time complexity of O(n * sqrt(n)) because we're checking all numbers up to `n` and then checking if each factor is prime. For large numbers, a more efficient solution using a prime factorization algorithm would be necessary.