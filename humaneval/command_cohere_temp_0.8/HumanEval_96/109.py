```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n` (`n` is the upper limit for the array). For each number `i`, it checks if `i` is prime using the `is_prime()` function and if `i` is less than `n`. If so, it adds `i` to the `primes` list and increments the `count` counter. Once the counter reaches `n`, it breaks out of the loop to stop generating more primes as the remaining ones will not be used. The function returns the `primes` list which is the solution for the given problem. 

To validate the functionality of the program, you can test it against the example outputs in the original problem description. 
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
```

The program should produce the expected outputs.