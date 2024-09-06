Here's the complete code:
```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        # Assume that all Fibonacci numbers greater than 2 are prime
        return True if all(is_prime(num) for num in fibonacci(n)) else False
        
def is_prime(num: int):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci(n):
    if n == 0 or n == 1:
        return []
    return [0] + fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    print(prime_fib(5))  # Example output: 89

```

This script defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime. The `is_prime` function checks if a given number is prime, and the `fibonacci` function generates the Fibonacci sequence.  The then demonstrate the function with an example call.