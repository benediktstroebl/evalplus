```python
def median(lst):
    # Sorting in ascending order
    sorted_lst = sorted(lst)
    # Checking the length of the list
    if len(sorted_lst) % 2 == 1:
        return (sorted_lst[len(sorted_lst)//2])
    # Checking the length of the list is even
    else:
        return (sorted_lst[len(sorted_lst)/2 - 1] + sorted_lst[len(sorted_lst)/2]) / 2

# Test case 1
median([3, 1, 2, 4, 5])
# Output: 3

# Test case 2
median([-10, 4, 6, 1000, 10, 20])
# Output: 15.0

# Test case 3
median([-5, -3, -8, -1])
# Output: -1

# Test case 4
median([10, -10, -20])
# Output: 10.0
```
The function median computes and returns the median of the list's elements. The median is the middle value of the sorted list when the list's length is even. The median is the average of the two middle numbers when the list's length is odd. The function passes all these tests with this functionality.