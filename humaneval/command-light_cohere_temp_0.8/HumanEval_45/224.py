```python
def triangle_area(a, h):
    return 3.14159 * a * (a**2 + h**2) **0.5 / 2

    assert triangle_area(5, 3) == 7.5, "Should be equal"
    assert triangle_area(6, 4) == 12.0, "Should be equal"
    assert triangle_area(8, 7) == 22.0, "Should be equal"
    ```