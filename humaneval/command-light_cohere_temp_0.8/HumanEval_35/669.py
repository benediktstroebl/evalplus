```python
def max_element(lst):
    if not_element(lst):  # Test for empty list
        return None
    if len(lst) == 1:
        return lst[0]
    max_val = float('-inf')
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

def not_element(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            return False
    return True
```