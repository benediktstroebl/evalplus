```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse * sin(acos(b / hypotenuse)) == a
```

The function calculates the length of the hypotenuse using the Pythagorean theorem and checks whether the given lengths form a right-angled triangle using the cosine rule. It returns 'True' if they form a right-angled triangle and 'False' otherwise, following the given criteria. 

Here is a simple test case to verify the functionality of the function:
```python
test_cases = [
    (3, 4, 5),
    (1, 2, 3),
    (7, 8, 10),
    (5, 12, 13)
]

for a, b, c in test_cases:
    assert right_angle_triangle(a, b, c) == True
```

Assuming the above is the desired solution. Feel free to modify or format it to your liking. Let me know if you would like me to explain any of the steps outlined in the code.