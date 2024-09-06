```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Note: you may assume the input is always valid
    if a < 0:
        a = abs(a)
    return a ** (1/3) == int(a ** (1/3))
```

This function `iscube` takes an integer `a` as input and returns `True` if `a` is a perfect cube, i.e., the cube of some integer. 

It verifies whether `a` is a perfect cube by taking its cube root (`a ** (1/3)`), and then checks whether the result is an integer (`int(a ** (1/3))`). If these two evaluations yield equal results, `a` is a perfect cube.

This approach leverages the characteristic of perfect cubes, where the cube root of a perfect cube yields an integer value. 

Additionally, it handles the case when `a` is negative by taking the absolute value, ensuring that the result is accurate for both positive and negative inputs. 

Note that this approach assumes that the input is always valid, as stated in the prompt. If the input value is not a valid integer, the provided code may not work as expected.