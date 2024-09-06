```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return n
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime and returns it. 

It first checks if the number is less than or equal to 1, in which case it returns n directly. It then checks if the particular number is 2 or 3, and returns 3 in such cases.

The code then starts a loop from i = 5, and checks if the square of the current value of i is less than or equal to n. This loop continues until the time i's square is less than or equal to n. 

The code then checks if the number is divisible by i or i + 2 without any remainder, and returns 0 in such cases. If the number is not divisible by i or i + 2, it means it's a prime Fibonacci number, and the function returns n. 
This function effectively calculates and returns the n-th Fibonacci number that is prime.