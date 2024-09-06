```python
def largest_prime_sum_of_digits(lst):
    primes = [x for x in lst if is_prime(x)]
    return sum(map(int, str(max(primes))))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_sum_of_digits(lst)` uses the `is_prime()` function to generate a list of prime numbers from the input list `lst`. Then it finds the maximum prime number and converts it to a string and sums up its digits to get the answer.