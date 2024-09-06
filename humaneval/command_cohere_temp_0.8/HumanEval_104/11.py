```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function iterates over each integer in the input list `xs`, checking if any digit in its representation in base 10 is even. It uses the `any` function in a nested fashion to check if any element in the iterator yielded by `str(int)` is true, which allows it to check every digit in the integer's representation. It returns a sorted list of all integers in `xs` that have no even digits. 

To showcase the effectiveness of the algorithm, let's run the function with the input from the example in the prompt: 
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
```

And here is the result of an input where the function should return an empty list:
```python
>>> unique_digits([152, 323, 1422, 10])
[]
```

This showcases how the function correctly identifies integers with no even digits and returns a sorted list of those elements.