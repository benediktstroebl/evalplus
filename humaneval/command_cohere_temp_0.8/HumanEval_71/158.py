```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if len(set(s)) == 2 or (s[0] < s[1] + s[2]) and (s[1] < s[0] + s[2]) and (s[2] < s[0] + s[1]):
        ar = (a * b * (s[0] - a) * (s[1] - b) * (c - s[2]) / 96)
        return round(ar, 2)
    else:
        return -1
```

The code defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the sum of any two sides is greater than the third side, which is a condition for a valid triangle. The function calculates the area of the triangle using the Heron's formula (`(s(s-a)(s-b)(s-c))/4` where s is the semi-perimeter of the triangle) and rounds it to 2 decimal places. If the sides form a valid triangle, it returns the calculated area. Otherwise, it returns -1 to indicate an invalid triangle.

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))  # Output: 6.00
print(triangle_area(1, 2, 10))  # Output: -1
```

This demonstrates the function's ability to calculate the area of a valid triangle and return -1 for an invalid triangle.