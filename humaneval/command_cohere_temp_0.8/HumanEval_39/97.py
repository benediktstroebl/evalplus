```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n < 1:
        return None
    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    for num in fib_nums:
        if is_prime(num):
            return num
    return None
```

The function `prime_fib` uses a list of Fibonacci numbers and loops through them to find the nth Fibonacci number that is also prime. The `is_prime` function is used to check if a number is prime.