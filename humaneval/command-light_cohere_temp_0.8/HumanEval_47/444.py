```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    elif len(lst) == 1:
        return lst[0]
    else:
        middle = len(lst) // 2
        left = median(lst[:middle])
        right = median(lst[middle:])
        return (left + right) / 2
``` 
This code defines a `median` function that computes the median of the elements in a given list `lst`. The function handles cases of empty or one element lists by raising `ValueError`. The function then determines the middle element count and divides the list into two even halves, calculates the median of the elements in each half, and returns the average of these medians.