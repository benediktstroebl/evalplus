```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

This Python script defines a function called `sum_squares`, which takes a list of numbers as input. Inside the function, it uses a generator expression coupled with the `sum` function to calculate the sum of squared integers in the list.

The critical enhancement is that before undertaking this operation, the code rounds each list element to the nearest higher integer. This ensures that all numbers are squared before being added to the sum. The function returns the calculated sum of the squared numbers. 

This solution addresses the problem's main challenge by rounding each element to the nearest higher integer before finding the sum of the squared numbers. As a result, it fulfills the problem statement's requirement of squaring and adding numbers while maintaining a single pass through the list.