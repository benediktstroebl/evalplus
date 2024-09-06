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
    prime_list = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            prime_list.append(i)
            count += 1
            if count == n:
                break
    return prime_list
```

This code contains two functions. The `is_prime` function checks if a number is prime. It handles the case when `n` is less than or equal to 1, then it iterates through integers from 2 to the square root of `n`, if at any point the number divides evenly with `i`, it returns `False`. If it doesn't encounter any divisors, it returns `True`. 

The `count_up_to` function uses the previously mentioned `is_prime` function to generate a list of prime numbers less than `n` and stops once it has collected `n` primes, or has exhausted all the prime numbers less than `n`. 

Here is an example usage of the above code:
```python
print(count_up_to(5)) # [2, 3]
print(count_up_to(11)) # [2, 3, 5, 7]
print(count_up_to(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(18)) # [2, 3, 5, 7, 11, 13, 17]
```

This would output:
```
[2, 3]
[2, 3, 5, 7]
[2, 3, 5, 7, 11, 13, 17, 19]
[2, 3, 5, 7, 11, 13, 17]
```

This demonstrates that the `count_up_to` function generates the correct list of primes as per the prompt.