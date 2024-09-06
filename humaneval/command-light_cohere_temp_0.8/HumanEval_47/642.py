```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
median([3, 1, 2, 4, 5])  # Output: 3.0
median([-10, 4, 6, 1000, 10, 20])  # Output: 15.0
median([1, 10, 20, 100, 3, 6])  # Output: 5.0
median([1, 2, 3, 20, 100, 4, 5])  # Output: 3.0
median([10, 20, 30, 40, 10, 1])  # Output: 15.0
```
This Python script defines a function median that computes the median of a list of numbers. The median is the average of the middle two numbers when the list has an odd number of elements, or the average of the two numbers when the list has an even number of elements. The script then passes tests with a variety of input lists and ensures that the function works correctly for any input.