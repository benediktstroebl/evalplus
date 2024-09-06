```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test suite
def test_incr_list():
    """Test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([])
    assert not incr_list([1, 2, 3, 4, 5])

if __name__ == "__main__":
    test_incr_list()
```
This code defines a function incr_list that takes a list l as input and returns a list with elements incremented by 1. The test_incr_list function contains a series of tests that verify the correctness of the incr_list function for different inputs. 

The code is self-contained, meaning it can be copied and pasted into any Python environment to run without additional dependencies, and it provides a clear and organized way to solve the problem and test the functionality.