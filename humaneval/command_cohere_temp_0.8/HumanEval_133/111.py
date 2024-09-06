```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares` serves to calculate the sum of squared positive integers in a given list. It works efficiently by employing a generator expression in conjunction with the `sum` function. This expression squares each element in the list that is both an integer or a float, and also positive. The result is a sum of squared values, ready to be returned. 

The function is optimized to process only relevant elements, reducing unnecessary computations. This is evident from the conditional checking an element's type and ensuring it's positive, which filter out irrelevant elements for calculating squared sums. This focused approach enhances performance and maintains a clean, concise code structure.