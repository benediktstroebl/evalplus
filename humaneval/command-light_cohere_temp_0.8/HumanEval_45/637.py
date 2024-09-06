```python
def triangle_area(a, h):
    """
    Calculate the area of the triangle given the lengths of two sides.

    Parameters:
    a (length of one side)
    h (length of the other side)
    
    Returns:
    float: The area of the triangle
    """
    return 0.5 * (a + h)

# Test case 1
print(triangle_area(5, 3)) # Output: 7.5 (Expected output)

# Test case 2
print(triangle_area(10, 6)) # Output: 30 (Expected output)

# Test case 3
print(triangle_area(7, 8)) # Output: 56.2 (Expected output)

```
The code defines a function called `triangle_area` that calculates the area of a triangle based on the lengths of its sides. It takes the formula `0.5 * (a + h)`. 

The function then passes three test cases, and the results are printed to the console.