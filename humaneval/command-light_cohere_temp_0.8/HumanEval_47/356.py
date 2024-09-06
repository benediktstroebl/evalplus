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
        if left_value > right_value:
            left, right = left_value, right_value
        else:
            left, right = right_value, left_value
        return (left + right) / 2

# Example usage
median([-10, 4, 6, 1000, 10, 20])
```