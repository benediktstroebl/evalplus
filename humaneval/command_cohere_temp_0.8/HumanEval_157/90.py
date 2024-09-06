```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Check for Pythagorean triplets
    if hypotenuse == c and a == b + c:
        return True
    elif hypotenuse == c and b == c + a:
        return True
    elif hypotenuse == a and a == b + c:
        return True
    elif hypotenuse == b and b == c + a:
        return True

    # If none of the conditions are met, return False
    return False
```

The function `right_angle_triangle` calculates the length of the hypotenuse and then checks if the lengths form any of the Pythagorean triplets. The Pythagorean triplet is a set of three positive numbers that meets the requirements for the hypotenuse in a right-angled triangle. The triplet can be arranged in a right-angled triangle. The function returns True if the sides form a right-angled triangle and False otherwise. 

This approach gives a concise solution and is more efficient than brute-forcing the angle calculation.