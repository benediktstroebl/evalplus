```python
def iscube(a):
    # Check if the number is a perfect cube
    return a ** (1/3) == int(a ** (1/3))
```

This function simplifies the problem by directly checking if the number can be expressed as a perfect cube, which are the integers that can be multiplied by themselves three times to yield the desired result. The equation a ** (1/3) == int(a ** (1/3)) checks if a is equal to the integer value obtained by rounding a ** (1/3) which are the operations needed for finding perfect cubes. 

For example, iscube(8) ==> (8) ** (1/3) ==> 2 == int((8) ** (1/3)) 
```bash
True
```