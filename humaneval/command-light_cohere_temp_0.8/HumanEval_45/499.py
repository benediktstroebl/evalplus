```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

#Test case 1: Verify the function
assert triangle_area(5, 3) == 7.5

#Test case 2: Verify the function with negative numbers
assert triangle_area(-5, 3) == -17.5

#Test case 3: Verify the function with floating point numbers
assert triangle_area(2.5, 6) == 43.25

#Test case 4: Verify the function with empty arguments
try:
    triangle_area()
except TypeError:
    print('Error: The function expects at least two arguments')
```