```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area, ensuring the triangle's validity with the semi-perimeter check. While the rounding is done with `round`, for full clarity, a `round` function call is additionally encapsulated within the function. 

This approach allows for easy integration with other scripts without the need for external function declarations, while also maintaining full functionality. 

Let me know if I can assist further or provide additional insights!