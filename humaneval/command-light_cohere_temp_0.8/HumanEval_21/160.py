Here's a Python script with a self-contained function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [0.0, 0.0, 0.0, 0.5, 0.5]
   0)  [0.0, 1.5, 2.5]
   0 and, 1.0)

    return [numbers[0.0, 0.5], 0.0, 0.5]
```

numbers = [0.5, 1.5, 2.5, 5.0, 0.5]

rescale_to_unit(numbers)

print(numbers) # [0.5, 1.5, 2.5, 5.0, 0.5]
print(rescale_to_unit(numbers))  # [0.0, 0.5, 0.5, 0.0, 0.5]

print(numbers[0] - res) for each element in numbers for i in range(1,6)]
```
The above Python script defines a function `rescale_to_unit` that takes in a list of numbers and returns a new list where each number has been rescaled to the range [0,1]. The numbers are rescaled by taking the difference between each element in the input list and the corresponding element in the output list, and subtracting that difference from each element in the input list.