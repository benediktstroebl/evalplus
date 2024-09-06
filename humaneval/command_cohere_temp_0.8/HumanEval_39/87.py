```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    if n <= 0:
        return None
    prev_fib, curr_fib = 1, 2
    for _ in range(n - 1): 
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    # checks for both prime and fibonacci criteria are done separately
    # this loop is needed only for the prime criterion
    for _ in range(n):
        if not is_prime(curr_fib):
            curr_fib += 1
            continue
        return curr_fib
``` 

This script defines a function `prime_fib(n)` that generates integers from the Fibonacci sequence and checks if each integer is prime. It uses the `is_prime()` function to check if a number is prime. 

The `prime_fib()` function starts by setting the previous Fibonacci number (`prev_fib`) to 1 and the current Fibonacci number (`curr_fib`) to 2. It then enters a loop that iterates `n - 1` times, updating the previous and current Fibonacci numbers accordingly. After the loop, it starts another loop, checking if the current Fibonacci number is prime. If it's not prime, it increments the number to try the next number in the sequence. If the current Fibonacci number is prime, it returns it. 

The `is_prime()` function checks if a given number is less than or equal to 1, it returns `False`. If the given number is 2 or 3, it returns `True`. For numbers exceeding 3, it checks for divisibility by 2 and 3. If the number is divisible by either, it returns `False`. Starting from 5, it iterates through numbers in increments of 6, checking for divisibility by 5 and 7 (i.e., checking if the number is divisible by i, or i + 2). If the given number is divisible by any of these, it returns `False`. If none of these conditions are met, it returns `True`.