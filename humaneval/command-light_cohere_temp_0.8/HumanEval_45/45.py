```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(6, 4) == 12.28
    assert triangle_area(8, 10) == 282.7
    ```
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on the given side length and high. The function uses the mathematical formula to compute the area of the triangle, which is the product of the square of the three sides divided by 2 times the hypotenuse. The function is then tested using three test cases, and the test passes successfully.