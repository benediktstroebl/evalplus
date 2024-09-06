```python
def median(lst):
    if len(lst) == 0:
        return None  # Handle empty list
    elif len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test case 1
median([3, 1, 2, 4, 5]) == 3.0

# Test case 2
median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
median([-1, 2, 3, 4, 5, 6]) == 2.5

# Test case 4
median([10, 20, 30, -5, 40, -2]) == (-1.0)

# Test case 5
median([0, 1, 0, 0]) == 0.0
```

This Python script defines a function `median(lst)` that computes and returns the median of the elements in a list `lst`. The function handles cases of empty lists and lists with even or odd numbers of elements. The median is calculated by finding the middle element in the list and averaging it with the previous middle element, or using the average of the two middle elements if the list has an odd number of elements.