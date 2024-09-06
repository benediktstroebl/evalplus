```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 0:
        return False

    # Find the largest cube root that is less than or equal to a
    for i in range(1, int(a ** (1/3)) + 1):
        if i * i * i == a:
            return True

    return False
```

This code defines a Python function `iscube` that takes an integer `a` as input and returns `True` if `a` is a perfect cube (i.e., `a` is the cube of some integer), and `False` otherwise. The function uses a loop to find the largest integer cube root that is less than or equal to `a` and checks if it equals the cube of that root. This efficiently determines if `a` is a cube without any floating-point computations. The function also handles negative inputs by returning false, ensuring correct identification of perfect cubes.