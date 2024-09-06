```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4] # True

# Test with nested list
assert incr_list([5, 3, 5, 2, 3, 3]) == [6, 4, 6, 3, 4, 4] # True

# Test with large range
assert incr_list([0, 123]) == [1, 2, 3] # True

# Test with different data types
int_list = [1, 2, 3]
assert incr_list(int_list) == [2, 3, 4] # True
str_list = ['a', 'b', 'c']
assert incr_list(str_list) == ['b', 'c', 'd'] # True

# Test with custom data structure
class MyData:
    def value: int
    def increment(self):
        self.value += 1

obj = MyData(10)
assert incr_list([obj]) == [obj.value + 1] == [11] # True
```