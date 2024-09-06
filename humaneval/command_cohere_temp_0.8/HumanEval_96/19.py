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
    prime_numbers = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_numbers.append(num)
            count += 1
            if count == n:
                break
    return prime_numbers
```

This script defines a Python function `count_up_to(n)` that solves the problem statement. It takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. 

The `is_prime(n)` function is used to check if a number is prime. It implements a simple primality test that checks if the number is less than or equal to 1, it returns `False`; otherwise, it iterates from 2 up to the square root of the number and checks if the number is divisible by any integer in that range, if it is, it returns `False`. If the loop completes without finding a divisor, it returns `True`. 

The `count_up_to(n)` function uses a loop to iterate through integers from 2 up to `n`, it checks if each integer is prime and if it's less than `n`, it adds it to the `prime_numbers` list and incrementates the `count` variable. Once `count` reaches `n`, it breaks out of the loop to stop counting. The final `prime_numbers` list is then returned. 

This solution is efficient and can solve the problem for reasonably large values of `n` within a reasonable time, but it's not the most efficient approach compared to more advanced primality testing algorithms. 

The unit tests are not provided since you mentioned they're already available. However, I can provide a sample test suite with relevant test cases to verify the correctness of the solution. 

Let me know if you'd like to include the test cases and discuss further optimizations if needed.