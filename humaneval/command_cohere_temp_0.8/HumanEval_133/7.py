```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
This function simply iterates over the list and accumulates the sum of squares of the elements directly. There's no need for rounding or complex logic, as the problem statement implies. The function signature is also simplified to def sum_squares(lst): instead of def sum_squares(self, lst): as there's no "self" argument to reference in this standalone context.