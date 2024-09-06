```python
def incr_list(lst):
    lst.+= 1
    new_item = lstool[0] + 1
    lst.append(new_item)
    return lst

# Tests
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert incr_list([5, 6, 7]) == [5, 6, 7]

# Main function to run the tests
if __name__ == "__main__":
    test_incr_list()
``` 
This script defines a function `incr_list` that increments the items of an input list by 1 and returns the updated list. The `test_incr_list` function tests the correctness of the `incr_list` function with various input lists.  The script also defines a main function that runs the test suite when the script is executed.