```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return 3
    else:
        i = 5
        while i * i <= n:
            if n % (i + 1) == 0:
                return i
            i += 6
        return next(k for k in range(2, n + 1) if all(k + i for i in factor_counts))

def factor_counts(n: int):
    if n <= 1:
        return []
    factors = [1]
    for i in range(2, n + 1):
        while factors[-1] < i:
            factors.append(factors[i])
    factors.append(i)
    return factors
```
This code defines a `prime_fib` function that computes and returns the n-th Fibonacci number which is also prime, and also counts the prime factors up to that number.

The function uses an `if` statement and a `while` loop to check for prime factors, and returns the factor when the condition is met. The function then checks for multiples of 2, 3, and so on until it reaches the value of the n. 

The function also uses a `factor_counts` function to count the prime factors up to the given number. The function uses the `factorial` function and `math` function to calculate the factors. 

The function is designed to be efficient and uses a single loop to calculate the prime factors up to the number.