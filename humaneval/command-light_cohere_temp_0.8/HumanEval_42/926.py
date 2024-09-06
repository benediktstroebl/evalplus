```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

#Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

#Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test1()
    test2()
```
This code defines a function `incr_list` that returns a new list with elements incremented by 1. The test cases demonstrate that this function correctly increments the elements in the list.

Note: The code is well-structured and self-contained, it can be easily imported and used in other Python scripts.