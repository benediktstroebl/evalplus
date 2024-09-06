Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the given number is less than 2, returning false immediately if so. It then iterates from 2 up to the square root of the number, checking whether the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false; otherwise, it returns true.

This algorithm covers edge cases like 1 and numbers less than 2, and follows a logical step of checking divisibility by the smallest potential divisors, reducing the chance of false positives. 

This function can be used to inform whether a number is prime or not, which can be useful in many situations, such as when checking if a number is suitable for use in a mathematical proof or when writing a program that requires a prime number as an input. 

The function is optimized to run efficiently, with the loop iterating only up to the square root of the given number, halving potential divisors with each iteration. 

This can be useful for sorting and filtering tasks which require identifying prime numbers.