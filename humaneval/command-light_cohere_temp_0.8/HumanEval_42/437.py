```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    
# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    
# Test case 3
def test3():
    assert len(incr_list([99, 100, 101])) == 3
    
# main execution
test1()
test2()
test3()
```

The code defines a function incr_list that takes a list l as input and returns a new list with elements from input list incremented by 1. It also has three test cases to validate the correctness of the incr_list function. The tests pass the language and are self-contained, so no external files are needed to solve this problem.