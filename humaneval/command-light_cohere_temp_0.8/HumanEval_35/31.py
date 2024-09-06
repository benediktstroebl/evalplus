```python
def max_element(lst):
    if not_negative_test(lst):
        return lst[-1]
    else:
        raise ValueError("Input list contains negative elements. In a list: [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
def not_negative_test(lst):
    return all(x >= 0 for x in lst)

print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```