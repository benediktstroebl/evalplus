```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1:
def test_get_positive():
    return [
        get_positive([-1, 2, -4, 5, 6]), 
        get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    ] 

# Test case 2:
def test_get_positive2():
    return [
        get_positive([9, -9, -1])
        , get_positive([1, 2, 3, -4, -5])
    ] 

test_get_positive()
test_get_positive2()
 ```