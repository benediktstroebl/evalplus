```python
def incr_list(lst):
    lst[:] = [x + 1 for x in lst]
    return lst

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test1()
    test2()
```
This code defines a function incr_list that takes a list lst as input and returns a new list with elements from the input list incremented by 1. The test1 functions test1 and test2 which pass the corresponding tests.