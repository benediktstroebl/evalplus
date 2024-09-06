```python
def incr_list(lst):
    return [n+1 for n in lst] 

# Test cases
test = unittest.py()
def test_incr_list():
    lst = [1, 2, 3]
    assert list(incr_list(lst)) == [2, 3, 4]
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert list(incr_list(lst)) == [6, 4, 6, 3, 4, 4, 10]
    lst = [5, 3, 'a']
    assert list(incr_list(lst)) == [6, 4, 'b']
test.inc()
```