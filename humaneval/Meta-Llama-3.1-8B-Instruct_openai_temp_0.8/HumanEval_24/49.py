```markdown
### Largest Divisor Function

This function finds the largest number that divides a given number n evenly, 
smaller than n.

#### Code

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number
    
    Returns:
    int: The largest divisor of n smaller than n
    
    >>> largest_divisor(15)
    5
    """
    
    # Starting from n-1, check each number if it divides n evenly
    for i in range(n-1, 0, -1):
        if n % i == 0:  # If n is divisible by i
            return i  # Return the largest divisor

# Test the function
print(largest_divisor(15))  # Output: 5
```

#### Explanation

This function works by iterating over all numbers smaller than n in descending order. 
As soon as it finds a number that divides n evenly (i.e., n % i == 0), it returns that number. 
This is because a larger divisor of n would also be a divisor of the larger number, 
so we don't need to check those. 

Note that this function assumes that n is a positive integer. If n can be negative 
or zero, you would need to add a check at the beginning of the function. 

Also note that this function has a time complexity of O(n), which might not be efficient 
for very large numbers. In that case, you could use a more efficient algorithm, like 
the one based on the prime factorization of n. However, for most practical purposes, 
this function should be sufficient.