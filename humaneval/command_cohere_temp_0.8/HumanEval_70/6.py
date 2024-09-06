```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = out.append(min(lst))
        lst = [x for x in lst if x != min(lst)]
        if len(out) > 1 and out[-2] == out[-1]:
            out.pop()
        else:
            max_idx = out.append(max(lst))
            lst = [x for x in lst if x != max(lst)]
    return out
``` 

The code starts with the minimum value and then finds the maximum value from the remaining numbers. It continues this process (using popping to prevent duplicates) until only one number is left, at which point it is added to the end. The solution is based on `append` operations to keep the list intact and minimize memory usage. 

The unit tests for this function are:
```python
def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([7, 2, 1, 3, 4, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert strange_sort_list([10, 10, 10, 22, 11, 12, 13, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 21, 22, 22, 22]

def test_empty_list():
    assert strange_sort_list([]) == []
``` 

The first test checks the basic cases, followed by a comprehensive test with a list of integers and a more extensive set of edge cases.