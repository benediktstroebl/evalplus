```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list `xs`, for each element `x`, it checks if any digit in the string representation of `x` is even, if such a digit is found, it skips the element, if no even digit is found, it includes the element in the resulting list, which is then returned. The sorting is applied automatically since we are using the built-in `sorted` function.