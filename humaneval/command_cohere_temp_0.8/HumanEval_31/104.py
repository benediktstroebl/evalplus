Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 up to the square root of the number, checking whether the number is divisible by any integer in that range. If the number is divisible by any of them, it returns `False`. However, if neither condition is met, it returns `True`, indicating that the number is prime. 

This implementation is efficient with a time complexity of O(sqrt(n)), where n is the given number. It is also reusable and self-contained, making it a versatile function to have for solving problems related to prime numbers.  It should serve as a robust foundation for solving prime number-related problems in tests and other scenarios. 

You can use this function in other parts of your code by simply calling `is_prime(n)` and passing the number you want to check for primality as an argument.  This will allow you to integrate it into your workflow and solve real-world problems that involve prime number checks efficiently.  It can be incorporated into larger functions or classes as a helper function to facilitate primality tests in dynamic and interactive ways.  This flexibility is a benefit of designing functions to solve specific problems in a self-contained manner, allowing them to be seamlessly integrated into diverse technical environments.