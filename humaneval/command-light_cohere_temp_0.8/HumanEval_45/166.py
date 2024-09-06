```python
def triangle_area(a, h):
    return 0.25 * (h** / 2) ** 2

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40
    assert triangle_area(15, 20) == 600

print("Passed tests: ")
print(test_triangle_area())
``` 
The code defines a function `triangle_area` that calculates the area of a triangle given its base and height. The `test_triangle_area` function contains asserts that check the correctness of the function by passing the test with the values 15, 10, and 4.2.