```python
def sum_squares(lst):
    result = sum(x**2 for x in lst if x % 1 == 0)
    return result
```

The function `sum_squares` takes a list of numbers `lst` as its input, it removes all elements with a decimal point and squares each element, finally, it sums all the squared elements and returns the result.