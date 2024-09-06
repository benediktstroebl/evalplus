```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l] 

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([1, 2, 3, 4, 5, 6]))) == 7
    assert incr_list([7, 8, 9, 10]) == [7, 8, 9, 10]
    assert incr_list([]) == []
    assert len(incr_list([55, 11, 13, 17])) == 4

if __name__ == "__main__":
    test_incr_list()
``` 
This code defines the `incr_list` function, which takes a list l as input and returns a new list with elements from l incremented by 1. The `test_incr_list` function tests the `incr_list` function by passing various input lists and checking if the result lists are correct. 

Finally, the code uses the `if __name__ == "__main__"` block to run the `test_incr_list` function when the script is executed.