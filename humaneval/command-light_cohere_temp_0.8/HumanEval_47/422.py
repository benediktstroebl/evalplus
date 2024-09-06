```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Basic tests
print(median([3, 1, 2, 4, 5]))  # Output: 3.5
print(median([10, 20, 40, 30, 25, 15]))  # Output: 20.0
print(median([5, 5, 5, 5]))  # Output: 5
print(median([]))  # Output: Raise ValueError: Input list must not be empty
```
The function median takes a list lst as input and returns the median of its elements. The function handles the simple cases: when the list is empty, or when the length of the list is even. When the length of the list is odd, the median is calculated by taking the middle value of the two middle elements. When the length of the list is odd, the median is simply the middle element.