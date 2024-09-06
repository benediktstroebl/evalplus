```python
def median(lst):
    """Return median of elements in the list lst"""
    return (len(lst) + 1)**.5 / 2 * (lst[int(.5 * len(lst))]] + lst[len(lst) // 2])

def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

def test_median_empty():
    assert median([]) == float('-inf')

def test_median_list():
    lst = [1, 2, 3, 4, 5]
    assert median(lst) == 3.0

def test_median_list_with_one_element():
    lst = [4]
    assert median(lst) == 4.0

def test_median_list_with_large_elements():
    lst = [1000, 1001, 1002]
    assert median(lst) == 1000.0

test_median()
test_median_empty()
test_median_list()
test_median_list_with_one_element()
test_median_list_with_large_elements()
```

The script defines a median function that computes the median of the elements in a given list. The function takes a list of numbers as input and returns the median as a floating point number. The test cases for the median function validate its correctness for different scenarios, such as with empty lists, one element lists, lists with a large number of elements, and passing lists of elements.