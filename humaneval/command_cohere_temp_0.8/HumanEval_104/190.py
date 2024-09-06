```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as input and returns a sorted list of all elements that do not have any even digits. The function uses a list comprehension to iterate through each element `x` in the input list `xs`, checking if any digit in the string representation of `x` is even. 

The `not any()` syntax flips the boolean result of any() to get a true value if all int(y) % 2 == 0 are false, i.e., there are no even digits in x.

If a digit is even, the element is filtered out of the list comprehension, and only the elements with no even digits are returned as a list and then sorted in ascending order.

This code can be tested as follows:
```python
# Test case from the problem statement
print(unique_digits([15, 33, 1422, 1]))  # Output: [1, 15, 33]

print(unique_digits([152, 323, 1422, 10]))  # Output: []
```
This would yield the correct results based on the problem statement.