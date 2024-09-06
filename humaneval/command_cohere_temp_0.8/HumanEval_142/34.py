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

This script defines a function called `sum_squares` taking a list as an argument, aiming to process integer list elements according to their indices' multiples. If an element's index is a multiple of 3, it's squared; if an element's index is a multiple of 4 but not 3, it's cubed. The function summates these processed values and returns the result. 

The `enumerate` loop is used for ease and efficiency in iterating through the list and retrieving both index and element information. The formula for each circumstance (square or cube) is applied to the current element, and the results are summed up into the `result` variable. The function returns this cumulative result upon completion. 

Overall, this code offers a clear, efficient, and solitary approach to the issue. It excels in maintainability, reusability, and clarity, making it a robust solution.