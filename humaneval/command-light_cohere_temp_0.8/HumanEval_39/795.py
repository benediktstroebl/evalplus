Here's the solution to the prompt:

```python
def is_fibonacci_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        num1 = 0
        num2 = 1
        for i in range(2, n):
            is_prime = True
            for j in range(2, int(i**0.25) + 1):
                if i % j == 0:
                    is_prime = False

            if is_prime:
                break

            num3 = j
        else:
            break
        return num3 == 2
```

This Python code defines a function called is_fibonacci_prime that checks whether a given number n is a prime Fibonacci number. 

The function first handles special cases: if n is less than or equal to 1, it returns False because prime numbers must be greater than 2. 

If n is 2, the function returns True since 2 is the only even prime number. 

For larger n, the function iterates up to the square root of n, using nested loops to check for divisibility by numbers from 2 up to the square root of n.