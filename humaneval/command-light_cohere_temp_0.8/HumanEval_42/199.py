```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]  # return a list with one more element and the same list 

# Test case 1:
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]  

# Test case 2:
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124] 
```  This code defines a function `incr_list` that appends 1 to the list and returns a new list with the incremented list. The code then provides two test cases that validate the correctness of the function.