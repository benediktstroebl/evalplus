```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
    else:
        return -1
```
The function first calculates the semi-perimeter of the triangle and then checks if the triangle is valid by comparing the semi-perimeter to the longest side. If the triangle is valid, the area is calculated using the Heron's formula (`(s * (s-a) * (s-b) * (s-c)) / 2`), and it is rounded to 2 decimal places. If the triangle is not valid, `-1` is returned. 

This solution allows you to accurately determine the area of a valid triangle with the provided lengths of its sides.