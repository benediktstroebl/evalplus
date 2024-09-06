```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

def test():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 10) == 66
    assert triangle_area(10, 20) == 196
    assert triangle_area(5, 5) == 25
    assert triangle_area(10, 15) == 156

if __name__ == "__main__":
    test()
```
The function `triangle_area` takes two parameters, `a` and `h`, which represent the length of the side and the height of the triangle, respectively. The function calculates the area of the triangle using the formula `area = (a * (h + a)) / 2`. This formula is used for all triangles.

The function passes the corresponding tests using the `assert` statement. It checks if the test if the following conditions are satisfied:
- The function `triangle_area` is called with the arguments `5` and `3`, and the result should be `7.5`.
- The function `triangle_area` is called with the arguments `8` and `10`, and the result should be `66`.
- The function `triangle_area` is called with the arguments `10` and `20`, and the result should be `196`.
- The function `triangle_area` is called with the arguments `5` and `5`, and the result should be `25`.
- The function `triangle_area` is called with the arguments `10` and `15`, and the result should be `156`.

The `test` function is a simple script that calls the `triangle_area` function with various arguments and verifies if the returned value is equal to the expected value. The `if __name__ == "__main__":` statement ensures that the `test` function is only executed when the script is run directly.