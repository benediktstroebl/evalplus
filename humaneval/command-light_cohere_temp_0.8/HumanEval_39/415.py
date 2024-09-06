```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    is_prime = True
    for i in range(3, int(n**0.5) + 1, :
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        return i
```
The function `prime_fib` returns the n-th Fibonacci prime number and is also prime. 

This function uses a simple algorithm to find the n-th Fibonacci prime number. It starts by checking if n is less than or equal to 1, in which case it is not prime. It then checks for the regularity in the Fibonacci sequence by trying divisibility from 3 up to the square root of n. Finally, it checks if n is divisible by any of these numbers to determine if it is prime or not.