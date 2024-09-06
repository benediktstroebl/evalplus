Here's the improved Python script with comments and a self-contained function:
```python
def is_prime(n):
    """
    Determine if a given number is prime.
    
    Args: n (integer)
    
    Returns: boolean indicating whether n is prime or not.
    """
    return n > 1 and all(n % i for i between 2 and int(n ** 0) )
```
The function 'is_prime' determines if a given number 'n' is prime or not. It returns 'True' if 'n' is a prime number and returns 'False' otherwise. This function is using a simple algorithm based on the knowledge that prime numbers are greater than 1 and divisible only by 1 and themselves.

Note: You can improve this function by adding more tests or optimizing the algorithm for larger inputs.