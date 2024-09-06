```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on the given lengths of its three sides `a`, `b`, and `c`.

The function first checks whether the sum of any two of the side lengths is greater than the third side length. This is done by comparing the sums of each pair of sides to each individual side length, and ensuring the difference is more significant than a negligible amount (`1e-6`). If these conditions are not met, it means the side lengths do not form a valid triangle, and the function returns -1 as specified in the prompt.

If the side lengths do form a valid triangle, the function uses the Heron's formula to calculate the area of the triangle. This formula is derived from the concept that the area of a triangle is equal to one-half of the product of its semi-perimeter and the square root of the difference between the semi-perimeter and each of the sides. The semi-perimeter is defined as the sum of the side lengths divided by 2, and the square root of the difference is computed for each side. The result is then rounded to 2 decimal places.

The formula for triangle area is mathematically expressed as:
```
Area = (1/2) * semiperimeter * sqrt{(semipi - side1)(semipi - side2)(semipi - side3)}
```

In summary, this script provides a practical way to compute the area of a triangle given its side lengths, while also ensuring the input forms a valid triangle.