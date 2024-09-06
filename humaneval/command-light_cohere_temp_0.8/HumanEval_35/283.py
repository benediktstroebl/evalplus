```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
tests = {
    "Test 1":
    list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(list1) == 123
   
 
    "Test 2":
    list1 = [1, 2, 3]
    assert max_element(list1) == 3
   
 
    "Test 3":
    list1 = [-5, -3, -10, -20]
    assert max_element(list1) == -10
   
}
```