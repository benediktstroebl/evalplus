```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function utilizes a list comprehension to filter out elements that are not greater than zero, resulting in a new list that contains only the positive numbers from the original input list. 

Such a concise solution is achievable due to the Python built-in syntax for list comprehension, which simplifies the task of creating a new list by applying a condition to every element of the original list.

This function can perform the task for any list input, regardless of the list size or complexity, as long as the elements in the list are numeric and can be properly filtered using the '>' operator.