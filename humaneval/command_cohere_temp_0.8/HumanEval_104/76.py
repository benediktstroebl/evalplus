```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an argument. It returns a sorted list of all elements `x` in the input list that do not have any even digits in their representation. The list is sorted in ascending order. 

The test cases are correctly provided in the original problem statement. Here we have added the code for the tests:
```python
# Test cases
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]
assert unique_digits([152, 323, 1422, 10]) == []
```