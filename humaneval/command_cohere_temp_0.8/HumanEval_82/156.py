```python
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    if len(string) <= 1:
        return False
    if is_prime(len(string)):
        return True
    return False
```

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 3, returning True if so. If the number is greater than 3, it checks if it can be divided evenly by 2 or 3, returning False if so. Next, it begins iterating through numbers of the form 6k ± 1, starting from 5 (note that divisors of prime numbers are of the form 6k ± 1, as all others can be expressed as a product of smaller primes). If the number is divisible by any such divisor, it returns False; otherwise, it returns True. 

The `prime_length` function calls `is_prime` on the length of the input string. If the length is prime, it returns True; otherwise, it returns False.

The test cases provided in the problem statement are handled correctly by the given solution.