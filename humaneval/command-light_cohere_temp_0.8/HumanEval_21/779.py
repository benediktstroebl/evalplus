Here's the solution you requested:

```python
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1 """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Define the rescaling function
    def rescale(num):
        return (num - min(numbers)) / (max(numbers) - min(numbers))

    # Apply the rescaling function to each element in the list
    numbers = [rescale(num) for num in numbers]

    return numbers
```

This Python code defines a function named `rescale_to_unit` that transforms a list of numbers so that the smallest value becomes 0 and the largest becomes 1. The function employs a list comprehension to apply the rescaling transformation to each element of the input list. This transformation ensures that the smallest number in the list is scaled down while the largest number is scaled down.  By applying this same same technique, the function achieves the desired result of scaling the numbers in the list while maintaining the relative order of the values.