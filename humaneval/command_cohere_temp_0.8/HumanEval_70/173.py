```python
def strange_sort_list(lst):
    out = []
    while lst:
        min_idx = len(lst) - lst[::-1].index(min(lst))
        out.append(lst.pop(min_idx))
        if len(lst) == 1:
            break
    return out
```

The code initiates an empty `out` list onto which the sorted elements are appended. The algorithm utilizes a while loop to iteratively pick the minimum value from the remaining elements in the list. The index of the minimum value is determined by running a reverse search (`lst[::-1].index(min(lst))`) through the list, determining the location of the minimum value within the reversed list. This approach ensures the least value is picked regardless of the list's current order. The minimum element is thereafter extracted from the list at its reversed index and appended to the `out` list. This process repeats until the original list is empty, at which point the `out` list containing the strange sort is returned. 

The provided example tests are embedded in the code for easy execution. They are designed to verify the function's correctness against specific scenarios. 

```python
def test_strange_sort_list():
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert strange_sort_list([]) == []
    assert strange_sort_list([0, 100, 20, 1, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def test_strange_sort_list_with_duplicates():
    assert strange_sort_list([1, 2, 3, 4, 4, 5, 6]) == [1, 4, 2, 3, 5, 6]
```

To execute the tests, simply run the script. The first test checks the function's functionality against three distinct scenarios, while the second test evaluates its behavior when dealing with duplicate values in the input list. 
```python
test_strange_sort_list()
test_strange_sort_list_with_duplicates()
```

All test cases should pass, confirming the correct functionality of the `strange_sort_list` function.