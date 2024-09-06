```python
def iscube(a):
    if a < 0:
        a = -a
    if a == 0 or a == 1:
        return True
    return (a**3) % 6 == 0
```

This function checks if the given integer `a` is a cube of some integer by performing the following steps:
1. If `a` is 0 or 1, it is a cube directly, so it returns `True`.
2. If `a` is negative, it converts the problem into a positive domain by calculating `(-a)`^3, which is equivalent to finding the cube of `a`.
3. It then checks if `a` is a cube by taking its cube root, `a^3`, and checks if it leaves a remainder of 0 when divided by 6. This is possible because all integers can be expressed as the cube of an integer, and the remainder of `(a^3)` modulo 6 will be 0 for all such representations.