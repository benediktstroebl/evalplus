```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer. It starts by handling the negative case by transforming 
`a` to its positive equivalent, then proceeds to raise it to the power of 3, and finally checks if the result equals the 
integer value obtained, without the use of `float`. 

This solution assumes that the input is always valid, as stated in the prompt. If zero testing is required, the user should 
modify the test cases accordingly.