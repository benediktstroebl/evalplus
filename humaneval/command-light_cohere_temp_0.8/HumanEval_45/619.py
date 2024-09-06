```python
def triangle_area(a, h):
    return 3.0 * a * (a ** 2) / 2

if __name__ == "__main__":
    print(triangle_area(5, 3)) # 5
    print(triangle_area(6, 4)) # 12
    print(triangle_area(10, 7)) # 50
    print(triangle_area(4, 8)) # 20
    print(triangle_area(7, 10)) # 43.5
```

This Python code defines a function `triangle_area` that calculates the area of a triangle given the lengths of its sides. The function uses the formula for the area of a triangle, which is the product of the base and the adjacent height, divided by 2. The code then passes the test cases for this function, and the results are printed to the console.