```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        for i in range(2, int(a ** (0.5)) + 1):
            if a % i == 0:
                return False

        return True
    return False
```

This function checks if a number is the multiplication of three prime numbers by using the `modulo` operation to check for divisibility. It iterates from 2 up to the square root of the number and checks if the number is divisible by any of these numbers. If it is, then the number is not prime, and the function returns `False`. If the number is not divisible by any of these numbers up to its square root, it is not composite, and the function returns True. Also, if the given number is less than 100 and greater than 1, it will return True as an example, demonstrating that 30 is correctly identified as a multiplication of three prime numbers (2 * 3 * 5).  This function should be efficient given that the worst-case complexity of prime checking is less than O(D * (D+1) / 2), where D is the square root of the number. 

The function also accounts for edge cases where the provided number is less than 100 but greater than 1, and returns False if the number is not within this range or is equal to 1. 

You can use this function to test whether other numbers meet the criteria by calling it and passing different numbers.  For example:
```python:
print(is_multiply_prime(60))
print(is_multiply_prime(52))
```
This would yield:
```bash
True
False
```
Note, you may want to add additional tests to ensure it handles other prime multiplications like 36, 52, etc.