```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function takes an integer a and checks if it is a perfect cube of some integer. It starts by checking if `a` is negative and if so, negates it since `-a` will be a cube of some integer if `a` is. It then cubes the integer and compares it to the originally cubed integer. If they are the same, it returns `True`. Otherwise, it returns `False`. 

This function assumes that the input is always valid, as stated in the prompt.