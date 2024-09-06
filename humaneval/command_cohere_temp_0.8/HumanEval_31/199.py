Here's a Python script with a self-contained function that solves the prime-checking problem, along with markdown code blocks that detail the approach and showcase the tests:
```python
def is_prime(n):
    """
    Checks whether a given number is prime.
    
    Args:
        n (int): Number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test Cases
# None of the below tests should raise an exception
# And all True results should be returned as expected
>> is_prime(6)
False
>> is_prime(101)
True
>> is_prime(11)
True
>> is_prime(13441)
True
>> is_prime(61)
True
>> is_prime(4)
False
>> is_prime(1)
False
```

This function handles edge cases (numbers less than or equal to 1, which are not prime) and iterates through potential divisors up to the square root of the number. 

The tests cover a range of scenarios, including prime and non-prime numbers, to ensure the function behaves as expected.