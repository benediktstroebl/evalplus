```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)) / 2, 2)
    else:
        return -1
```

The function follows the description in the prompt: the semi-perimeter is calculated, and then compared to the maximum side length; the area is calculated using Heron's formula if the condition is met, and -1 is returned otherwise. The rounding to two decimal places is handled using the `round` function. 

To handle numerical stability, especially with floating-point numbers, it's advisable to compute the square root last, without storing the intermediate results in variables, as illustrated in the code. 

This approach allows the function to handle edge cases, such as triangles with very large or very small sides, while maintaining accurate area calculations.