```python
def triangle_area(a, h):
    return max(3.0*a, h*(a+h) for a in [1,2,3,4,5])
```
The triangle_area function takes two parameters, a and h, and returns the area of a triangle with sides of length a and h. It uses a max function with a nested list of tuples, which contains the lengths of the triangle sides. This function also passes them test, which is a function that takes a and h as parameters and returns True if a < h and h < a, which means that the triangle sides are in decreasing order.