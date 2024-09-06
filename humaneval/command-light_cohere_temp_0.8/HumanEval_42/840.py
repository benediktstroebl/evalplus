```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
def test3():
    l = [5, 3, 5, 2, 3, 3]
    assert incr_list(l) == l  # Should return l itself, shouldn't modify input list

if __name__ == "__main__":
    test1()
    test2()
    test3()
```
This script provides a function `incr_list` that returns a new list with elements incremented by 1. The test cases are then used to verify the correctness of the function. The final part includes a `if` statement, which indicates that the script is running as a standalone program. 
This structure ensures that the function and tests are self-contained, making the solution clean and organized.