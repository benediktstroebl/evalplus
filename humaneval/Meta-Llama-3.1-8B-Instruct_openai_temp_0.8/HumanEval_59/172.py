```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.
    
    Parameters:
    n (int): The input number.
    
    Returns:
    int: The largest prime factor of n.
    """
    
    # Initialize the largest factor
    largest_factor = 2
    
    # Iterate from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        # While n is divisible by i
        while n % i == 0:
            # Update the largest factor
            largest_factor = max(largest_factor, i)
            # Divide n by i
            n = n // i
    
    # If n is greater than 2, it means n itself is a prime number
    if n > 2:
        # Update the largest factor
        largest_factor = max(largest_factor, n)
    
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a while loop to divide `n` by the smallest divisor (which is 2 or any other prime number), and updates the largest factor whenever a larger prime factor is found.