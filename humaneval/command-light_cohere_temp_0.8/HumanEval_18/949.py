```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.
    """
    prime factor
    prime factors of a number are the factors for which it is divisible by 2.
    """
    first_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    counter = 0
    for prime in first_primes:
        counter += (string.contains(substring) / (prime))
    return counter

# Test the function
string = "aaaaaaa"
substring = "aa"
print(how_many_times(string, substring)) 
```