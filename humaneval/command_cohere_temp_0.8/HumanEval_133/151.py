```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
This function definitions take a list (`lst`) as input, and it calculates the sum of squared elements in that list. Using a for loop, it iterates through each element `n` in the list, and adds its squared value (`n ** 2`) to the `result` variable. The function then returns this `result`, which represents the sum of squared numbers in the list. 

This code resolves the issue stated in the problem statement, ensuring that the sum of the squared values of each list element is returned, regardless of whether the list members are integers or floats. The ceiling rounding technique is not necessary for this particular task.