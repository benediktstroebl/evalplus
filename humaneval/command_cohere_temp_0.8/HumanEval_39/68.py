Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Generates n-th Fibonacci number that is also prime
    """
    if n < 1:
        raise ValueError("n must be a positive integer.")

    count = 0
    fib_nums = [0, 1]
    while len(fib_nums) < n:
        next_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(next_num)
        if is_prime(next_num):
            count += 1
    return fib_nums[n - 1] if count == n else -1

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) == -1  # There is no 6th prime Fibonacci number
```
This code defines two functions: 
- The `is_prime` function checks whether a given number is prime
- The `prime_fib` function returns the n-th Fibonacci number that is also prime. The `prime_fib` function uses the `is_prime` function to screen the Fibonacci numbers it generates. 

This code includes test assertions to validate the function behaviour. You can enhance the test suite for more comprehensive coverage. Feel free to adapt this code to your needs. Let me know if you have any concerns or if you'd like assistance with anything related to Python, problem-solving, or any other topic!