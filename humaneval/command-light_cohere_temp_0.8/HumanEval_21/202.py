Here's the solution to the problem:

```python
def rescale_to_unit(numbers: List[float]):
    return [x / min(numbers) for x in numbers] if numbers else [x * 1.0 for x in numbers]
```

This function applies a linear transformation to the list of numbers, such that the smallest number will become 0 and the largest will become 1. It uses the Python list comprehension and the min() function. The function also uses the list comprehension and the * 1.0 operator to multiply numbers by the unit 1, which ensures that the resulting values are positive and fall within the unit [0, 1].]

This function is self-contained and can be used directly to solve the problem. It can also easily be imported into a Python script and called as a method.