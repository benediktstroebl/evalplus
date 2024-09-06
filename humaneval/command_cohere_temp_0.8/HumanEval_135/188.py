```python
def can_arrange(arr):
    largest = -1
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            largest = i+1
    return largest
```
The function `can_arrange` sorts the input array and then iterates over the non-greater-than-or-equal elements in the sorted array, tracking the largest index of such an element and returning -1 if none are found. 

Here is a test suite to ensure the function behaves correctly:
```python
def test_can_arrange():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([5, 5, 4, 3, 9, 2, 1]) == -1
    assert can_arrange([7, 8, 9, 10, 11, 12, 13]) == 5
    assert can_arrange([0, -1, -3, -4, -11, -14]) == -1
```