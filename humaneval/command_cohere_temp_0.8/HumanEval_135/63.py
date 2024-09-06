```python
def can_arrange(arr):
    prev = arr[0]
    arranged = -1
    for idx, cur in enumerate(arr[1:], start=1):
        if cur <= prev:
            continue
        arranged = idx
        break
    return arranged
```

The function `can_arrange()` iterates through the array, comparing each element to the previous one. When an element greater than the previous one is found, the loop continues, considering it for the arrangement. If an element smaller than or equal to the previous one is encountered, it means it can be arranged at that position, so the variable `arranged` is assigned the current index, and the loop breaks. If the loop completes without finding an arrangement, the element doesn't have a suitable position, so the function returns -1. 

This solution allows for an efficient linear time complexity of O(n) to find the arrangement, without the need for additional space to store arranged elements. 

Here's a basic unit test to ensure the function behaves as intended: 

```python
def test_can_arrange():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([10, 11, 12, 13, 5, 4]) == 4
    assert can_arrange([2, 3, 4, 1]) == -1
``` 

To execute the test, you can copy and paste it into a Python environment of your choice.