```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

This Python script defines a function called `get_positive` that takes a list as an input parameter. It uses a list comprehension to filter out only the elements in the input list that are greater than zero, effectively isolating the positive numbers. 

The function returns a new list that contains the positive numbers from the input list, disregarding any negative or zero values. 

This solution is concise and adheres to Python's PEP 8 style guide, as it uses descriptive naming and whitespace for readability. 

You can test this function with examples similar to those given in the problem statement to verify its behavior. 
For example:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
``` 

This would yield the expected output, providing a filtered list of only the positive numbers from the given input lists as illustrated in the original problem statement. In the two test examples provided in the original problem statement, the function is applied to a list of various numbers, including both positive and negative values. The function is designed to filter out only the positive numbers from the input list, and it does so effectively in both cases, producing the expected output.  This further reinforces the correctness of the function.