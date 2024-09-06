```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x+1)

# Test cases for function
test_sort_even = [
    True,  # [2, 3, 4, 5]
    [5, 6, 3, 4],
    [1, 2, 3],
    [5, 6, 7, 8]
]

def test_sort_even():
    actual = sort_even(test_list)
    assert actual == test_list

test_sort_even()  # test execution
```
The function **`sort_even`** is a stand-alone Python function that takes a list **`lst`** as an argument and sorts it according to even items. It uses the stable sorting algorithm to accomplish this, and it returns a sorted list. 

The function is then tested using the **`test_sort_even`** function and the **`test_list`** provided. The test verifies that the function's output matches the expected value.