```python
def triangle_area(a, h):
    return sqrt(a * (h + abs(a - h)))

# Test case 1: Function succeeds for triangle with side length 5 and height 3
assert triangle_area(5, 3) == 7.5

# Test case 2: Function succeeds for triangle with side length 10 and height 7
assert triangle_area(10, 7) == 49.25

# Test case 3: Function succeeds for triangle with side length 5 and height 7
assert triangle_area(5, 7) == 28.6

# Test case 4: Input arguments are not equal
with pytest.raises():
    pytest.fail_call = [triangle_area, '5', '3')
    assert pytest.false_call() < 1e
```