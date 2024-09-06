```python
def max_element(lst):
    if not_numbers(lst):
        return "Input list must contain numeric values"
    return max(lst)

def not_numbers(lst):
    return any(map(float, lst))

print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```