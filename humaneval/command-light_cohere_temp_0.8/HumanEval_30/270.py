```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test suite
def test():
    input_list = [-1, 2, -4, 5, 6]
    assert get_positive(input_list) == [2, 5, 6]
    input_list2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
    assert get_positive(input_list2) == [5, 3, 2, 3, 9]

# Main execution
test()
```