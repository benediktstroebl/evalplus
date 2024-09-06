```python
def triangle_area(a, b, c):
    s = sum(i for i in [a, b, c] if i < sum(j for j in [a, b, c] if j != i))
    if len(s) > 0:
        return round(0.5 * (a * b * scipy.gcd(a, b) / 2), 2)
    else:
        return -1
```
The function `triangle_area` takes in three parameters, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The logic to check if the triangle is valid is done using a list comprehension; it checks if the sum of any two sides is greater than the third side. The validity of the triangle is then checked with the condition `len(s) > 0`, where `s` is the list of sides that do not satisfy the criterion that the sum of any two is greater than the third. The function returns -1 if the triangle is not valid and the rounded area (to 2 decimal places) if it is.

To test this function, a simple script could include two test cases like so:
```python
import numpy as np
import scipy

np.random.seed(0)
a = np.random.random()
b = np.random.random()
c = np.random.random()
print("random triangle", triangle_area(a, b, c))

a = 3
b = 4
c = 5
print("structured triangle", triangle_area(a, b, c))
```
This will test the function with a random set of sides as well as a structured set of sides.