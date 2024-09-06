Here's a self-contained Python function that solves the problem of scaling numbers in a list:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [5.0, 0.0, 10.0, 2.0]
    result in the5
    numbers 
    numbers = [num * 2.0 / 1.0 for num in numbers]
    return numbers
```

This function takes a list of numbers as input and returns a new list with the numbers in the original list but each value multiplied by 2/1 and divided by 1. 

The function first creates a list of numbers [5.0, 0.0, 10.0, 2.0] that are used in a list of numbers with the same value. Then the function applies a list of numbers by multiplying each number by 2/1 and dividing it by 1. Finally, the function returns the list of numbers.