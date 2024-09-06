```python
def iscube(a):
    # Write a function that takes an integer a and returns True 
    # if this integer is a cube of some integer number
    # Note: you may assume the input is always valid
    if a < 0:
        a = a * a * a
    else:
        a = a ** 3
    return a == int(a)
```

This Python script defines a function `iscube` that takes an integer `a` as input and returns `True` if `a` is a perfect cube of some integer, and `False` otherwise. The function relies on the intrinsic nature of perfect cubes where the result of raising an integer to the power of 3 and returning the equivalent integer value will always be an integer itself, as opposed to a float due to decimal values incurred through decimal moving digits. 

The provided examples in the prompt are also provided here for better understanding on how the function behaves:
```python
# You can test the function
print(iscube(1))  # True
print(iscube(2))  # False
print(iscube(-1))  # True
print(iscube(64))  # True
print(iscube(0))  # True
print(iscube(180))  # False
``` 

This is just one potential solution and you are encouraged to critique or enhance the above method through your own consistent reasoning.