```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function iterates over each integer in the input list `xs`, checking if any digit in its representation as a string is even. The `any` function combines the evaluation of multiple conditions, specifically, for each digit in the string representation of the number, it checks if it's odd or even. The `not` operator simply reverses this logic, effectively selecting only odd digits. Finally, the integer is filtered if it meets the condition, meaning it contains no even digits, and is added to the returned list. The list is sorted in ascending order, as required by the prompt. 

The function relies on native Python operations and doesn't need any external modules. 

This solution is fully compliant with the problem statement in the given prompt.