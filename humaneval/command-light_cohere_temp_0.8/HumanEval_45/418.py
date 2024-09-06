```python
def triangle_area(a, h):
    return 3.14 * (a** / 2) ** 2 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Should return 5 for this triangle with sides of 5 and 3"

def test_non_negative_input():
    a = 0
    h = 10
    assert triangle_area(a, h) == 0, "Area should be 0 for non-positive sides"

if __name__ == "__main__":
    test_triangle_area()
    test_non_negative_input()
```
This code defines a function called `triangle_area` that calculates the area of a triangle based on its side lengths. The `test_triangle_area` function checks if the result of `triangle_area` matches the expected value for a triangle with sides of 5 and 3. The `test_non_negative_input` function verifies that the area is zero when the side length is zero, which is the correct result. 
This code follows the standard style of writing tests for functions, using the `assert` keyword to define test cases and asserting the function's output matches the expected result.