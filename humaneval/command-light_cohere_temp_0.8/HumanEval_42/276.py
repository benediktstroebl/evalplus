```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l

def test_incr_list():
    """Test the incr_list function"""
    lst = [1, 2, 3]
    result = incr_list(lst)
    assert len(result) == 6
    assert all(result > [0])  # Elements should be 1 or greater
    assert result == [2, 3, 4]

def main():
    """Function to call test_incr_list"""
    test_incr_list()

if __name__ == "__main__":
    main()
``` 
The code includes a function `incr_list` that adds 1 to the last element of the input list, and a test function `test_incr_list` that checks the correctness of the `incr_list` function by passing it a test list. The `main` function is used to execute the `test_incr_list` function and is responsible for initializing the list.