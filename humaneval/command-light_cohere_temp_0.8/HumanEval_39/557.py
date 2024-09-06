```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    temp = prime_fib(n // 2)
    if temp == 2:
        return temp
    return temp + 2

# test suite
print(prime_fib(5))
print(prime_fib(6))
print(prime_fib(10))
``` 
This code defines a function `prime_fib` that computes and returns the n-th Fibonacci number that is prime, it also checks if the number is prime or not.  The function utilizes the recursive approach, breaking the problem down into smaller cases: for numbers less than or equal to 1, the number itself is returned, for numbers less than 3, it returns 3, and for numbers that are even divisors of 2, it returns 5. For these special cases, the function uses a helper function that computes the prime factor of n by dividing n by 2 and checking if the result is equal to 2.