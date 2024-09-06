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
    prime_list = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_list.append(num)
            count += 1
            if count == n:
                break
    return prime_list
```

This script defines a function `count_up_to()` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. The function initializes an empty array `prime_list` to store the prime numbers and iterates through numbers from 2 up to `n`. It checks each number using the `is_prime()` function to determine if it is prime. If the current number is prime and less than `n`, it is appended to `prime_list`, and the `count` variable is incremented. The loop continues until `count` reaches `n`, at which point it stops iterating. 

The `is_prime()` function is also included and checks if a given number is prime by iterating through numbers from 2 up to the square root of the input number `n`, and checking for divisibility. If the number is divisible by any integer within this range, it is not a prime number, and the function returns `False`. If the number is not divisible by any integer within this range, it is a prime number, and the function returns `True`. 

This solution includes both functions working together to solve the problem statement.