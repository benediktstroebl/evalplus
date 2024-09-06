```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an argument. It returns a sorted list of all elements `x` in the input list that do not have any even digits in their representation. The list is sorted in increasing order. 

The algorithm employs a list comprehension that iterates through each element `x` in the input list `xs`. For each `x`, it checks if any digit in the string representation of `x` is even. The expression `int(y) % 2 == 0` checks if a digit `y` is even, and when combined with `any()` function, it returns `True` if at least one digit in `str(x)` is even. The list comprehension returns only those elements for which the condition is satisfied. Finally, the function sorts the resulting list in ascending order. 

The unit tests in the script test the function with examples from the problem statement and an additional test to verify that the function behaves correctly when an empty list is passed in. 
```python 
# Tests:
assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
assertEqual(unique_digits([152, 323, 1422, 10]), [])
assertEqual(unique_digits([]), [])
``` 
This code adheres to Python's style guidelines with consistent use of parentheses, and descriptive variable names, making the code readable and maintainable.