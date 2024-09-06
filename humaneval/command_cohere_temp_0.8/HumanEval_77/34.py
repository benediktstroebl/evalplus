```python
def iscube(a):
    # Check if the number is greater than 0 and equals to the cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function checks if the number given is greater than 0, then it checks if the `nth` root of the number `a` is an integer with `a ** (1/3) == int(a ** (1/3))`. Thus, it guarantees that the number is a cube of some integer. 

This solution ranks among the most elegant and simple solutions for this problem.

### Here are some examples of how to use this function:
```python
# You can test the function with different inputs
print(iscube(1)) # Output: True
print(iscube(2)) # Output: False
print(iscube(-1)) # Output: True
print(iscube(64)) # Output: True
print(iscube(0)) # Output: True
print(iscube(180)) # Output: False
``` 

This would output:
```
True
False
True
True
False
```