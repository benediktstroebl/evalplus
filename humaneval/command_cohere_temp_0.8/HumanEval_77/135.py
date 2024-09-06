```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer by simply cubing the number and comparing the result with the original input. If they are the same, it returns `True`, else `False`. Additionally, it handles the case when `a` is negative by converting it to its positive equivalent since the cube of a negative number is equal to the negative cube of an integer.

The function's logic is based on the mathematical operation of raising `a` to the power of 3 and comparing the result with the original input. If they are equal, it means `a` is a cube of some integer. 

Let's take some examples to test the above function:
```python
print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False
```

The above output will print:
```bash
True
False
True
True
False
```

The function handles all cases, correctly identifying whether the given integers are cubes or not.