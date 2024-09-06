```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to iterate through each element `x` in the input list `xs`, checking if any digit in the string representation of `x` is even. The list comprehension constructs a new list with only the elements from `xs` that do not have any even digits, which is then sorted in ascending order and returned.

Here is a snippet of test cases that can be used to validate the functionality of the code:
```python
# Test case 1
assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

# Test case 2
assert unique_digits([152, 323, 1422, 10]) == []

# Test case 3
assert unique_digits([11, 33, 55, 59, 99, 100, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == [11, 33, 55, 59, 99, 222, 333, 444, 555, 777, 888, 999, 1000]
``` 
This will ensure that the function `unique_digits` works as expected, sorting the list in ascending order and including only those elements that have no even digits in their representation.