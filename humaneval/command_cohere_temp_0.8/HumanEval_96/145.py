```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `is_prime` function is used to check if a number is prime. This function checks if the number is less than or equal to 1, in which case it immediately returns false. It then iterates through the numbers from 2 to the square root of the number and checks for divisibility. If the number is divisible by any of these integers, it returns false. If it is not, it returns true.  The `count_up_to` function uses the `is_prime` function to iterate through numbers from 2 to `n`, it checks each number if it is prime and if it is smaller than `n`, it adds it to the `primes` list and increments the `count` variable. Once the count reaches `n`, it breaks out of the loop to stop generating more primes.  The output of the function corresponds to the example tests provided in the prompt.