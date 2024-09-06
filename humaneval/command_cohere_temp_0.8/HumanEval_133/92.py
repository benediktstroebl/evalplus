```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares` that takes in a list of numbers (`lst`) as input. Within the function, it uses a generator expression alongside the `sum` function to calculate the sum of squared integers in the list `lst`. The generator expression iterates over the elements in the list, and for each element `x`, it checks if `x % 1 == 0`. This condition ensures that only integer values are considered, disregarding any non-integer values. For eligible integers, their squares (`x ** 2`) are calculated and added to the result. Finally, the function returns this computed sum of squared integers. 

Note: this approach assumes that the list contains only integer values or floats that can be rounded to integers. It might not work as intended with lists containing other data types or non-roundable floats. 

The script assumes the presence of required tests files in the directory, and it can be imported as a module in the specific Python environment where it is executed.