```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list is empty")
    elif len(lst) == 1:
        return lst[0]
    else:
        middle = len(lst) // 2
        left_value = lst[middle - 1]
        right_value = lst[middle]
        return (left_value + right_value) / 2
``` 
This code defines a function `median` that calculates the median of a list `lst`. It handles cases with an empty list or a single element, and in the general case, it divides the middle element with its previous and next elements to calculate the median.