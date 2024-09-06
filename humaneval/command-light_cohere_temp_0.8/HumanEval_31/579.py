```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
This function determines whether a given number is prime or not, passing all the test cases provided in the prompt.

You can use this is_prime function to solve the problem for different numbers. It is a solution that checks each prime number up to sqrt(n) and returns True if any of those primes are found, else False.

This approach ensures that the function has full self-contained behavior with respect to input and output, and does not require any external functions or variables for its correctness.