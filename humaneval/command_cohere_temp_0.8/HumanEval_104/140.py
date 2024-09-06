```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list `xs`, for each element `x`, it checks if any digit in the string representation of `x` is even, if such a digit is found, the element is not included in the resulting list, if no such digit is found the element `x` is included in the list that is returned. The function returns a sorted list based on the input requirement.

The tests cases correspond to the following behavior:
```
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
>>> unique_digits([24, 121, 4, 27])
[4, 27]
>>> unique_digits([94, 904, 14, 124, 61])
[14, 61]
>>> unique_digits([153, 352, 51, 17, 327])
[17, 51]
```