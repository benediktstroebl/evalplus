```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total == 180:
        return True
    else:
        return False
```

This function evaluates the sum of the triangle's sides. If the sum is equal to 180, then the triangle is right-angled, whereas, it returns False otherwise. 

To ensure effectiveness, this function assumes that the inputs are the lengths of the three sides of the triangle. 

Also, ensure that the sum of the lengths does not exceed 180 to avoid false negatives. You can tweak the function to your needs, such as adding unit tests or improving its flexibility regarding input validation. 

Lastly, the function's current design adheres to the problem's prompt, achieving the intended functionality in an optimized manner.