```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of a triangle using the Pythagorean theorem, threfore it returns `True` if they form a right-angled triangle and `False` otherwise. It is important to note that the function assumes the lengths provided are integers or at the very least reciprocals of integers to deal with the cases where the lengths are unequal to the hypotenuse naturally exist. 

This approach gives a brute-force solution to the problem and should be acceptable for most cases. There are other optimizations that can be applied to make the function faster but it is important to note that those will make the function a bit more complex and less self-contained. 

It is also worth noting that the function correctly identifies the right-angled triangle irrespective of the order of side lengths provided.