```python
def iscube(a):
    # Check if the number is divisible by 2 and itself at the same time
    if a % 2 == 0 and a ** (1/3) == int(a ** (1/3)):
        return True
    # If the number is not divisible by 2, then it must be a prime number
    elif a == 1 or a % 2 != 0:
        return a ** 3 == int(a ** 3)
    else:
        return False
```

This function utilizes a modular exponentiation approach to determine if `a` is the cube of an integer. If `a` is not divisible by 2, it must be a prime number, and therefore the only way for it to be a cube is if it is multiplied by itself three times. Otherwise, if `a` is divisible by 2, it is sufficient for it to be multiplied by itself once (`a ** (1/3)`). The function then checks if this value equals the integer value of the cube root (`int(a ** (1/3))`). 

This algorithm achieves a time complexity of O(log(a)), where a is the given number.