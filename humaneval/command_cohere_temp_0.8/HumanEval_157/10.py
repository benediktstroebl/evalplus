```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that the sum of the squares of the two legs of a right-angled triangle must equal the square of the hypotenuse, to determine whether the triangle is a right-angled triangle. 

Here is an example usage of the function:
```python
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
```
This example would print True and False respectively, as in the given examples, the first set of lengths forms a right-angled triangle whereas the second set does not. 

This algorithm is brute-force and performs no further optimizations. It is efficient in terms of both time and memory as it only computes the squares of the inputs and performs a simple comparison.