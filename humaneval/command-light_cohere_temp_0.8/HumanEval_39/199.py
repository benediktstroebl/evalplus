```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    i = 5
    while i * i <= n:
        if n % (i + 2) == 0:
            return i
        i += 6
    return i + 2
``` 
This Python function, `prime_fib`, calculates the nth Fibonacci number that is prime. It returns the for any numbers 1, 2, and 3, as they are the first three prime numbers. It also checks for numbers that are divisible by 2 and returns 5. It then iterates through the the previous method, which uses the square root rule to find the next prime number, and since the square root of any prime number is greater than the original, it iterates inwards up to the square root.