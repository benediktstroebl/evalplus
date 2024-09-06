```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal
    to the values of the even index of l, but sorted."""
    return [x if x % 2 == 0 else x[::-1] for x in l]

# tests
def test_sort_even():
    assert sort_even([1, 2, 3]) == [1, 2, 3]
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# main program
if __name__ == "__main__":
    test_sort_even()
```
The script defines a function **sort_even(list)** that returns a new list with elements from the input list that match the condition of being an even index, are swapped. This function is use a array unpacking and a simple condition to achieve this.

The script then includes a test function **test_sort_even()** that checks if the **sort_even** function works correctly for two test cases. The **if __name__ == "__main__":** line at the end of the script runs the test function.