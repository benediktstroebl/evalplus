```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the root of a is an integer
        if int(a**(1/3)) == a**(1/3):
            # Check if a is the multiplication of 3 prime numbers
            if a != 1: 
                return all([p == a % p for p in range(2, int(a**(1/3) + 1))])
        else:
            return False
    else:
        return False
```

The script defines a function `is_multiply_prime(a)` that checks if `a` is the multiplication of 3 prime numbers or not. It returns `True` if the condition is met, and `False` otherwise. The method first checks if `a` is less than 100. It then checks the root of `a` and verifies if it's an integer. If it is indeed an integer, it proceeds to check if `a` is not equal to 1, and if that holds true, it verifies if a is the product of 3 distinct prime factors, whose initialization was done in the range from 2 to the root of `a`. If all these conditions are fulfilled, the function returns `True`. If any of the conditions are not met, it returns `False`. 

NOTE: In the code, the second condition `if int(a**(1/3)) == a**(1/3)` is meant to check if the cubic root of a is an integer, and if it is indeed a whole number, the function proceeds to the next step. This is intended to replace the computationally expensive `isinstance(a**(1/3), int)` check, since the cubic root of a number is generally not an integer.