```python
from collections import deque
def prime_fib(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fibonacci(n):
        fib = deque([0, 1])
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[n-1]

    if n <= 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return fibonacci(n//2)
    return fibonacci(n) if is_prime(fibonacci(n)) else prime_fib(n+1)
```

This script defines two helper functions:
1. `is_prime`: This function checks if a given number is prime or not. It checks if the number is less than 2 or if it has any divisors between 2 and the square root of the number. 
2. `fibonacci`: This function generates the Fibonacci sequence by using a deque (double-ended queue) to store the elements, as this data structure allows efficient prepending elements to the sequence. The function continues adding numbers until the deque contains `n` elements, which is the index of the desired Fibonacci number. 

The `prime_fib` function handles the edge cases `n=1,2,`, and `n%2==0`, and falls back to either calculating the average Fibonacci number or checking the primality of subsequent numbers until it finds the n-th prime Fibonacci number. 

Note that this approach has a time complexity of `O(2^n)` as it checks all odd Fibonacci numbers until it finds the n-th prime one, and a space complexity of `O(n)` to store the `n` Fibonacci numbers in the deque.  This technique may not be the most efficient approach for large n, but it uses basic primality testing and Fibonacci sequence principles.  If you have specific large n values in mind, I can optimize the approach further!