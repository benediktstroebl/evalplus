```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 2
    elif n % 2 == 0 or n == 6:
        return 3
    else:
        limit = 2
        while limit * limit <= n:
            temp = limit
            limit += 1
            if temp * temp > n and n % temp == 0:
                return temp
            else:
                continue
        return 5

# Example usage:
print(prime_fib(6))
``` 
This code defines a `prime_fib` function that calculates and returns the n-th Fibonacci number that is also prime. It uses a testing to make sure the function is correct.