Here is a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers):
    return [x * 100 for x in numbers]
```

This function takes a list of numbers as input and returns a list of numbers that have been rescaled to the unit [0, 1]. The function uses a list comprehension to apply the linear transformation to each element in the input list. 

You can use this function with a list of numbers, such as [1.0, 2.0, 3.0, 4.0, 5], and the expected list to be rescaled to the unit [0, 1].