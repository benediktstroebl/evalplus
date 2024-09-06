```python
def iscube(a):
    # Check if the number is greater than 0
    if a < 1:
        return False

    # Find the greatest factor f of a which is also a cube
    for i in range(2, int(a ** (1/3)) + 1):
        if a % i == 0:
            f = i
            while a % f == 0:
                a //= f
            if a == 1:
                return True

    return False
```

The problem prompts you to write a function that takes an integer `a` and returns `True` if `a` is a cube of some integer. To identify the cubes of integers, we need to consider the integer's factors. The core idea is to find the largest factor `f` of `a` that is also a cube. Factors are numbers that divide `a` evenly. For example, `90` has factors `[1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90]` which means that these numbers can be multiplied to give `90`. We are looking for a factor cube representation like this: `a = f * f * f`. From the factor list, we can identify `f = 6` as the largest factor which is also a cube. Then we iterate through the factors and divide `a` evenly by `f`. In the end, if `a` equals `1`, it signifies the existence of a cube factor representation, and the function returns `True`. If no such factor is found or `a` equals `0`, the function returns `False`.