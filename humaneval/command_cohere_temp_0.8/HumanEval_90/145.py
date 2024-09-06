```python
def next_smallest(lst):
    lst.sort()
    if len(lst) < 2:
        return None
    else:
        return lst[-2]
```
This approach takes advantage of Python's built-in sorting capability, which allows the list to be sorted in place. Since the list is sorted, the second smallest element is at the second position, which is accessed using lst[-2]. If the list has less than two elements, the function returns None.

Here's the inline test harness:
```python
def test_next_smallest():
    assert next_smallest([1, 2, 3, 4, 5]) == 2
    assert next_smallest([5, 1, 4, 3, 2]) == 2
    assert next_smallest([]) == None
    assert next_smallest([1, 1]) == None
test_next_smallest()
```
This test harness verifies that the function `next_smallest` behaves as expected according to the problem's statement.