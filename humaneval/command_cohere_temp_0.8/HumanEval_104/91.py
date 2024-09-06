```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
This Python script defines a function `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list and returns a sorted list of all elements `x` that do not contain any even digits in their representation. The function uses a list comprehension to iterate through each element `x` in the input list `xs`, it checks if any digit in the string representation of `x` is odd using the `any` function and a generator expression, if there are no odd digits (i.e., all digits are even), then `x` is added to the `result` list. Finally, the function sorts the `result` list in ascending order and returns it.

Here is an example usage of the function implementing the note:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```
These examples test the function with valid inputs and expected outputs. The first example returns `[1, 15, 33]` because all digits are odd; in contrast, the second example returns an empty list because all elements have at least one even digit in their representation.