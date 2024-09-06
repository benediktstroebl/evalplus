```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single equality operation and uses the **int()** function to remove the decimal points of the cube root. It assumes that the input is a valid integer and does not check for invalid input.

However, a more comprehensive solution would be to use **numpy** to solve this problem, as the **numpy** library provides the exact cube root of a number using **numpy.ceil**. **numpy.ceil** returns the smallest integer that is greater than or equal to a given number. This is how you can use it:
```python
import numpy as np

def iscube(a):
    result = np.ceil(a ** (1/3))
    return result == int(result)
```
Which would be the recommended approach for this problem.