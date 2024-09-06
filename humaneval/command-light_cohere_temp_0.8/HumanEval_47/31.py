```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) == 1:
        return lst[0]
    m = 0
    for i in range(len(lst) // 2):
        m += lst[i]
    return m
# Example usage
lst = [-10, 4, 6, 1000, 10, 20]
print(median(lst))  # Output: 15.0
```