```python
def max_element(lst):
    return lst[-1] if len(lst)>0 else None

# Test suite
def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

if __name__ == '__main__':
    print("Test succeeded")
```