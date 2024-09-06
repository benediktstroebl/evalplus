```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return i
            i += 1
        return i + 1

# Example usage
print(prime_fib(5))
``` 
This script defines a function, `prime_fib`, that computes the n-th Fibonacci number such that it is prime and iterates up to the nth term. The function uses an efficient method of dividing the number into its prime factors and adding 2 to the result.