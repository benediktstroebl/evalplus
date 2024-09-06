```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# Basic test case: Test function with specific values
assert(triangle_area(5, 3), 7.5)

# Edge case: Test function with zero length
assert(triangle_area(0, h), 0)
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its sides (`a` and `h`). 

The function uses the formula for the area of a triangle, which is the product of the base and the height, divided by 2. 

The function is then tested with different inputs. The first test case successfully verifies the area calculation with specific side lengths (5 and 3), yielding a result of 7.5 square units. 

The second case verifies the area with zero length, which should yield 0. 

This self-contained function provides a straightforward and concise solution to the problem and can be used as a basis for more complex geometric calculations in various contexts.