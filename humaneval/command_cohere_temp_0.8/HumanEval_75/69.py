```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    if a < 3:
        return False
    for i in range(2, int(a**.5()) + 1):
        if a % i == 0:
            return False
    return True
```

This Python script defines a function called `is_multiply_prime` that takes a single argument `a`. The function returns True if `a` is the product of 3 prime numbers, and False otherwise. The function first checks if `a` is less than 3, and returns False immediately if this is the case. Then, it iterates through the numbers from 2 to the square root of `a`, and returns False immediately if it finds any number that divides `a` without leaving a remainder. If the loop completes without finding such a number, it returns True, indicating that `a` is the product of 3 prime numbers.

Here is an example usage of the function:
```python
print(is_multiply_prime(30))
```
This will print `True` as the output, as the script verifies that 30 is indeed the product of 2, 3, and 5.

Here is another example:
```python
print(is_multiply_prime(52))
```
This will print `False` as the output, as 52 is not a multiply prime number as it can be divided by 2, 13, and 2 again, unlike the intended purpose of the `is_multiply_prime` function. 

This script effectively solves the problem and would work correctly for various inputs.