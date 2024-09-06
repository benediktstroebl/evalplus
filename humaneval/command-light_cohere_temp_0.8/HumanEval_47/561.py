```python
def median(lst):
    # sort the list in ascending order
    lst.sort()
   
    elements in sorted order.
    # calculate theIT median of the middle two elements
    middle1 = lst[len(lst) // 2]
    middle2 = lst[(len(lst) + 1) // 2]
    if len(lst) % 2 == 1:
        return middle1
    else:
        return (middle1 + middle2) / 2

# test case
test_median = [10, 20, 4, 6, 3, 1]
median(test_median) # 20.0
```