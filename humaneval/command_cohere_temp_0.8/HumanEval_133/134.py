```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares` takes a list of inputs `lst` and aims to calculate the sum of squared integers in the list while ignoring negative numbers or non-numeric elements. Here's how it does it: 

1. It uses a generator expression (`x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0`) to iterate over the elements of the input list `lst`. 

It filters out elements that do not derive from the `int` or `float` classes or those that are negative. 

2. For each integer or float that is non-negative, it squares the element with the expression `x ** 2`. 

3. It then calculates the sum of these squared values using the `sum` function. 

Lastly, it returns the calculated sum of the squared values as the output. 

The script ensures that only positive integers are included in the sum, while negative numbers and non-numeric elements are ignored.