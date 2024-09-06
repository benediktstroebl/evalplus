```python
def triangle_area(a, h):
    return 3.14 * a * * (a**2 + h**2) **0.05

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 4) == 50.2
```
The code defines a function `triangle_area` that calculates the area of a triangle based on the length of two sides (`a` and `h`) using the formula `*(a^2 + h^2) / 4`. 

The `test_triangle_area` function is used to test the `triangle_area` function with different inputs. It checks if the's result is equal to the expected value.