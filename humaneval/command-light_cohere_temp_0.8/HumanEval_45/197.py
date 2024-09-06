```python
def triangle_area(a, h):
    return 3 * (a * (h + a)) ** 0.25

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.8
    assert triangle_area(10, 5) == 62.6
    ``` 
``` 
This code defines a function called triangle_area that calculates the area of a triangle given the lengths of two of its sides. The function uses the mathematical formula for the area of a triangle, which involves the sum of the squares of the sides.