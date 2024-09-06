```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a, b = 2, 3
        for _ in range(5):  # b shall always be odd
            a, b = b, a + b
            if a == b:
                break
            else:
                if a % b == 0:
                    break
        return a
```
This function uses a basic approach to generate the n-th Fibonacci number that is prime. It checks for the parameters like a <= 1 and 2, and then starts a loop where it adds the two numbers together until they become a prime (which means the product is not equal to the other).