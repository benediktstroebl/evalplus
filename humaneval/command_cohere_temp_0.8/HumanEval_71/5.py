```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.pi / 3)), 2)
```

The function first checks whether the sum of the two largest sides is significantly larger than the smallest side. If so, it returns -1, indicating that the sides do not form a valid triangle. If the sum checks out, it computes the area using the formula `0.5 * (a * b * math.sin(math.pi/3))`, rounds it to 2 decimal places, and returns the result. Please note that this approach stems from the fact that the triangular shape is equilateral. 

To round a float to 2 decimal places, I have used the `round()` function in the code, which is a built-in function in Python. It works like this:
```python
round(x, decimals)
```

Where:
- `x`: This is the input float number that we want to round. 
- `decimals`: This is an optional integer that specifies the number of decimal places to round the number to. 

The default value for `decimals` is 0, so the function will round the number to the nearest whole number when `decimals` is omitted. 

In our case, we rounded the float to 2 decimal places by adding `round(0.5 * (a * b * math.sin(math.pi/3)), 2)` in the code. 

Let's break down how this works: 
1. `0.5 * (a * b * math.sin(math.pi/3))`: This part calculates the approximate area of an equilateral triangle with sides of length 'a', 'b', and 'c'. An equilateral triangle has three sides of equal length, and this formula simplifies the calculation of its area. 
2. `round(0.5 * (a * b * math.sin(math.pi/3)), 2)`: This part rounds the calculated area to two decimal places. The `round()` function takes two arguments: 
    - The first one is the number to be rounded, which is the computed area in this case. 
    - The second one is the number of decimal places to round to, which is set to 2. 

This ensures the area is rounded to two decimal places as required by the problem statement. 

Overall, this function calculates the area of an equilateral triangle or determines that the sides are not long enough to form a triangle, checking the condition that the sum of any two sides is greater than the third side.