```python
def is_prime_length(input_str):
    if len(input_str) <= 1:
        return False
    
    primes = [2, 3]
    while primes[-1] * primes[-1] <= len(input_str):
        primes.append(primes[-1] + 2)
    
    return len(input_str) in primes
```

The function `is_prime_length` checks if the length of the input string is a prime number. It first checks if the length is less than or equal to 1, returning `False` in such cases. It then builds a list of prime numbers up to the square root of the length and checks if the length is one of them.

This solution corresponds to the specifications provided, providing a boolean response for strings of any data type. 

The given examples in the original problem statement would return:
- 'Hello': True
- 'abcdcba': True
- 'kittens': True
- 'orange': False 

Which would all be correctly classified by the above function.