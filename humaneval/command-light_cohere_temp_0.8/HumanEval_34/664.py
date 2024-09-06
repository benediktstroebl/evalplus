```python
def unique(l: list):
    seen = set()
    return [element for element in l if element not in seen and element not in [-0, None)]

# Test case 1
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

# Test case 2
class Test:
    def test(self):
        lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        assert unique(lst) == [0, 2, 3, 5, 9, 123]

test = Test()
test.py()
```