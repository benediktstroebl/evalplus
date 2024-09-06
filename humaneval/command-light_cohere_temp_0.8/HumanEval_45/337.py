```python
def triangle_area(a, h):
    return 3.14 * (a** * h)

if __name__ == "__main__":
    a = 5
    h = 3
    result = triangle_area(a, h)
    print(f"Result: {result}")
```

The function takes two parameters, `a` and `h`, which represent the lengths of the sides of the triangle. The function calculates the area of the triangle by multiplying the lengths of the sides with the square of the hypotenuse. The calculated area is then returned as the result.