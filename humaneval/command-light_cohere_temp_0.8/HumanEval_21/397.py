Here's a self-contained Python function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    numbers = [x / 100.0 for x in numbers]
    numbers.append(min(numbers)+1)
    return numbers
```

This function receives a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The result is then a list of numbers with values between 0 and 1.

The function works as follows:
- The function takes a list of numbers as input.
- It then applies a linear transformation to the list, such that the smallest number in the list becomes 0.
- Then function then creates a new list with the same elements, but with the elements divided by 100. This effectively scales down the0 numbers so that they are all between 0 and 1.
- Finally, the function adds 1 to the smallest element in the list. This ensures that the smallest number becomes 0 and all the other numbers become positive.

This function can be used to solve the problem of resizing numbers in a markdown code block.