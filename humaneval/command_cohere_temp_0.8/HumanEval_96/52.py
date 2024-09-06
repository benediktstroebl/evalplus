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

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to confirm if it's a prime number and if it's less than `n`. If it is a prime number, it adds it to the `primes` list and increments the `count` variable. Once the `count` variable reaches `n`, it breaks the loop to ensure the function only collects the first `n` prime numbers.

To demonstrate the behavior of the problem, let's run the script with different inputs and test its behavior:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
```

The script produces the following output:
```
[2, 3]
[2, 3, 5, 7]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[]
[2, 3, 5, 7, 11, 13, 17]
```

This list contains the first few prime numbers for each input, as requested in the prompt.