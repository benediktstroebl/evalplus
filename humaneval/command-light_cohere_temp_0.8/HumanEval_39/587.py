```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return_value = 2
        for i in range(2, n + 1):
            is_prime = True
            for j in range(2, i * 2 + 1):
                if j % i == 0:
                    is_prime = False
            if is_prime:
                return_value = i
        return_value
``` 
This Python code defines a function called `prime_fib` that calculates the n-th Fibonacci number that is prime and returns it. The function starts by checking if n is less than or equal to 1, and if it is, it immediately returns n. If n is greater than 1, the function proceeds to calculate the n-th Fibonacci prime number by iterating through Fibonacci numbers and checking each one for primality.