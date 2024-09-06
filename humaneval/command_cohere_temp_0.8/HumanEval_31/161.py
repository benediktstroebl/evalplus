Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The algorithm used is the `Sieve of Eratosthenes`, which is an efficient way to find all prime numbers up to a given integer. The `range` function is used in the step where the function iterates through all the numbers from 2 up to the square root of the input number `n`, and returns `False` if any of them can divide the input number `n`. This accurately follows the problem statement and the given tests. 
The tests assert the behavior of the `is_prime` function for different input cases.

Here is a step-by-step explanation of the algorithm:
1. The function first checks if the given number n is less than 2. If it is, the function returns False, as numbers less than 2 are not prime.
2. The function then iterates through all the numbers from 2 up to the square root of the given number n using the range function. 
3. The function then checks if any of these numbers divide the given number n. If any of them do, the function returns False, as numbers that have divisions other than 1 and themselves are not prime.
4. If the loop completes without finding a divisor, the function returns True, indicating that the given number is prime. 

This algorithm is highly efficient as it only requires checking divisors up to the square root of the given number. Furthermore, the function's simplicity and ease of understanding make it ideal for solving the prime number determination problem.