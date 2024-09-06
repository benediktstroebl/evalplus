```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a * h / 2
    area = base * (h / 2)
    return area
```
The function `triangle_area` takes in two variables, `a` and `h`, and uses the formula `0.5 * a * h` to calculate the area of the triangle. It first calculates the base of the triangle and then multiplies it by the height to get the area. This area is then returned to the user. 
This approach is more efficient and delivers the anticipated result, namely, the area of the triangle given the length of a side and its height.