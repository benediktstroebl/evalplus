Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
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
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            primes.append(num)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number to the `primes` list and incrementing the `count` variable. When `count` reaches `n`, it breaks out of the loop, returning the list of prime numbers that are less than `n`.

You can test this function by calling it with different input values and comparing the results to the examples provided in the problem statement. Here is an example of how you can use the function:
```python
print(count_up_to(5)) # [2,3]
print(count_up_to(11)) # [2,3,5,7]
print(count_up_to(20)) # [2,3,5,7,11,13,17,19]
print(count_up_to(0)) # []
print(count_up_to(1)) # []
print(count_up_to(18)) # [2,3,5,7,11,13,17]
``` 

This will output the following:
```
[2, 3]
[2, 3, 5, 7]
[2, 3, 5, 7, 11, 13, 17, 19]
[]
[]
[2, 3, 5, 7, 11, 13, 17]
```

This indicates that the function correctly solves the problem for the provided examples.