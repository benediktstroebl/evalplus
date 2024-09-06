Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def double_the_difference(lst):
    odd_and_positive = [x for x in lst if x > 0 and isinstance(x, int) and x % 2 != 0]
    return sum(x * x for x in odd_and_positive)
```

This function uses a list comprehension to filter out odd, positive, and integer values from the input list. Then, it doubles the value by squaring in the sum function to find the sum of squares. The result is the sum of the squares of odd integers up to and including the given value. 

Here is an example of an invocation for this function:
```python
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
```

This function will run correctly for the test cases mentioned in the prompt, as it handles the stated rules correctly.  For example, it returns 0 for an empty list, filters out negative numbers, and only processes integer values.