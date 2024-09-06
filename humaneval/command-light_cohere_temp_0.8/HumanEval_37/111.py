```python
def sort_even(l: list):
    """Sorts a list to ensure all even indices are in order.
    l.append(0, if index is even an even index, i. have an index to be equal"""
    if not i%2 == 0:
        l.append(l[i])
    else:
        l.append(l[i+1])
    return l
    """

def test_sort_even(test_list):
    test_list = list(test_list)
    result = sort_even(test_list)
    assert result == [3, 6, 5, 4]
    assert result == [2, 3, 4, 5]
    assert result == [1, 2, 3]
```
The function takes a list as input and returns a sorted list of even indices. The function uses a append to add the next element to the list if the index is even, and otherwise, it adds one more element to the list.

The test function creates a list, then calls the sort_even function with the list as an argument, and checks that the function's output is equal to the expected output.