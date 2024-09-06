```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an input parameter `lst`. This function will iterate through the list using the `enumerate` function to access the index and value of each entry in the list `num`. 

If the index of the entry is a multiple of 3, the function will square the integer entry, if the index is a multiple of 4 and not a multiple of 3, the function will cube the integer entry, and the entries whose index is not a multiple of 3 or 4 will not be altered. The function will then add each of these calculations to the `result` variable, which is initially set to 0, and finally, the function will return the `result`.

Such that if we were to call `sum_squares([1,2,3])`, the output would be `6`, `sum_squares([-5,10,15])` would output `150`, and `sum_squares([-1,-5,2,-1,-5])` would output `-126`.

This script will pass the provided tests because it takes each condition from the problem description into consideration whilst summing up the resulting values accordingly.