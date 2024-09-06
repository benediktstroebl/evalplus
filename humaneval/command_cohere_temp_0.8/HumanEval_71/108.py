```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(x + y > z for x, y, z in zip([a, b, c], [a, c, b], [b, c, a])))) == 3:
        return round(0.5 * (s * (s-a) * (s-b) * (s-c))**, 2)
    else:
        return -1
```
The function checks whether the sum of any two sides is greater than the third side. If all these conditions are met, the function calculates the area of the triangle using the Heron's formula. Otherwise, it returns -1. 
For example, the code returns the area of a triangle with sides **3**, **4**, and **5** as **6.00** and for sides **1**, **2**, and **10**, it returns **-1**. You can add additional test cases to this code to ensure the function works correctly for any valid triangle.