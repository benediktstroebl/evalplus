```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that solves the problem as outlined in the prompt. It iterates through each element in the input list `xs`, and for each element `x`, it checks if any digit in the string representation of `x` is even. If no even digit is found, the element is included in the `result` list. Finally, the function returns a sorted list of these filtered elements.