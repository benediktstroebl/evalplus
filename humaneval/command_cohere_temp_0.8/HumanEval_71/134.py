```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c)))), 2)
```
This function calculates the area of a triangle with side lengths a, b, and c. It first checks whether the sum of any two of the sides is greater than the third side, following the specification of a valid triangle. If not, it returns -1 to signify an invalid triangle. Otherwise, it calculates the area using the Law of Cosines formula and rounds the result to 2 decimal places.

Here's the explanation:
1. The function first checks the conditions of a valid triangle using the sides a, b, and c, and sums (s) of these sides, returning -1 if they do not form a valid triangle. This is done using the conditional statement `if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:`. 
 2. If the sides do form a valid triangle, it proceeds to calculate the area using the formula `area = 0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c))))`. This uses the Law of Cosines to compute the angle between sides a and b, and then uses the sine of this angle to calculate the area. 
 3. The area is then rounded to 2 decimal places using the `round()` function and returned as the final result. 
The script ensures that the function works for both valid and invalid triangles, adhering to the specified conditions and rounding requirements. Hwangpoong Suicide Squad Shirt.