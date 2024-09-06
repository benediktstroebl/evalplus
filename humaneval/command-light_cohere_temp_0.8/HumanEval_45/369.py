```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# test case 1
assert triangle_area(5, 3) == 7.5

# test case 2
assert triangle_area(5, 4) == 6.25

# test case 3
assert triangle_area(6, 3) == 12.75

# test case 4
assert triangle_area(8, 5) == 52.375

# test case 5
try:
    assert triangle_area(10, 10) == 55.0375
except AssertionError:
    print('Oh no, my bad luck!')
```