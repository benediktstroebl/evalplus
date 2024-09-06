```python
def iscube(a):
    # Check if the number is divisible by 2 and itself at the same time
    if a % 2 == 0 and a ** (1/3) == int(a ** (1/3)):
        return True
    # If the number is not divisible by 2, then it must be a prime number
    elif a == 1:
        return False
    elif a % 2 != 0:
        # Check if the number is divisible by 3 and itself at the same time
        if a % 3 == 0 and a ** (1/3) == int(a ** (1/3)):
            return True
        else:
            return False
    else:
        return False
```

This Python script defines a function `iscube` that takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer, and `False` otherwise. 

The function checks if `a` is divisible by 2 and if `a` is divisible by 3, performing the cube root calculation only if the number is divisible by 2 to avoid false negatives for prime numbers. 

This approach ensures that the function accurately identifies perfect cubes while preventing unnecessary computations for non-cubes.