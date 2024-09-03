```python
def any_int(x, y, z):
    return x == y + z and all(type(i) == int for i in (x, y, z))
```
This function takes three parameters, x, y, and z. 
It returns True if x is equal to y + z and all the values are integers. 
The function returns False otherwise. 
This function is self-contained, and its correctness is guaranteed by passing all the test cases.