Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a compact way of creating a new list based on existing lists, to filter out all positive numbers from the input list `l`. The result is a new list that contains only the positive numbers from the input list. 

The `if` statement in the list comprehension checks if each element `x` in the list `l` is greater than zero `> 0`, and if it is true, it includes `x` in the new list.

The resulting list comprehension returns `[]` if the input list is empty. 

This solution is efficient as it utilizes Python's list comprehension, which naturally handles iterating through lists and filtering elements in a single pass. Thus, its performance is optimized for both speed and memory usage.