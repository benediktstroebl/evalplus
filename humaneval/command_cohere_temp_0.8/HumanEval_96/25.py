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
    """Return an array of the first n prime numbers less than n"""
    count = 0
    primes = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

The `is_prime` function checks if a given number is prime or not. Then the `count_up_to` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime` function and appends the prime numbers to the `primes` list. The `count_up_to` function stops when it has collected `n` prime numbers or when it reaches `n` itself. 

To better understand the code, here is an example of using the `count_up_to` function:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
```

The provided example outputs illustrate the behavior of the `count_up_to` function for the specified input values.