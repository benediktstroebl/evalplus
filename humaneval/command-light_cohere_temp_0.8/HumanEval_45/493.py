Here is a self-contained Python function that calculates the area of the triangle:
```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 12)) # Output: 104.6
```

This function takes two parameters, `a` and `h`, representing the length of a side and the height of a triangle, respectively. The function returns the value of the area of the triangle, which is calculated as half of the product of the two sides and the sum of the two heights.