```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst.append(1)
    return lst

def test_incr_list():
    """Test the incr_list function"""
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    got = incr_list(lst)
    assert expected == got

# Run the function and test it
incr_list(lst)
test_incr_list()
```
This script defines a function `incr_list` that increments the elements of a given list by 1 and a test function `test_incr_list` that validates if the `incr_list` function works correctly by checking if the returned list matches the expected output. 
When you run the script, it will create and print the output.

The `incr_list` function works by appending the value 1 to each element of the list and then returns the updated list.