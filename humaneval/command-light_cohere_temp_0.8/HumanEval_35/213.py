```python
def max_element(lst):
    if not_unique(lst) == False:
        return "Input list must be unordered"
    if len(lst) == 0:
        return "Input list cannot be empty"
    if not_integer(lst) or not [type(num) == int for num in lst]:
        return "Input list must contain only integers"    
    return max(lst)

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 123
    assert max_element([-10, 0, 1]) == 1
    assert max_element([5, -10, 3]) == 3
    assert max_element([-100, -20, -15]) == -15
    assert max_element([21, 18, 9]) == 9
    assert max_element([-1, -10, -9, -100, -20]) == -100
```
The above Python script defines a function max_element that calculates the maximum element in a list. The test_max_element function provides test cases to ensure the correctness of the max_element function.