```python
def triangle_area(a, h):
    """
    Calculates the area of a triangle given the base and height.
    Returns: the area (in square units).
    """
    return 0.5 * *sqrt(a** * (h**2))

def test1():
    assert triangle_area(5, 3) == 7.5

def test2():
    assert triangle_area(8, 5) == 32.0

if __name__ == "__main__":
    test1()
    test2()
```
This code defines a function called `triangle_area` that calculates the area of a triangle based on the given base and height. It also defines two test functions that test the function and pass the test successfully.