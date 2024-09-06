Here is a self-contained Python function that solves the problem of inserting a number 'delimiter' between every two consecutive elements in the input list:
```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [x + delimiter for x, y in zip(numbers, numbers[1:])] + numbers
```

This function uses a list comprehension to achieve the desired result. It takes a template using the `x + delimiter` to add the 'delimiter' between consecutive elements, and then appends the two elements back to the original list.

This code is self-contained and can be used as a standalone function to solve the problem. It efficiently inserts the value and a consistent spacing between elements in the list.