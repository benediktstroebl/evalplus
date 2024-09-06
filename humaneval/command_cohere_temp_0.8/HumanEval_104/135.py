```python
def unique_digits(xs):
    return sorted([x for x in xs if not any(int(y) % 2 == 0 for y in str(x))])
```
This function `unique_digits(xs)` takes a list of positive integers, `xs`, as an input and returns a sorted list of all elements that do not have any even digits. This is done using a list comprehension that iterates over each element in the input list, `xs`, and checks if any digit in each integer `x` is even. 

Here is an example usage of the function:
```python
print(unique_digits([15, 33, 1422, 1, 324]))
```
The function will return the list `[1, 15, 33],` which are the only elements in the given list that do not have any even digits. 

This approach utilizes Python's filtering and transformation capabilities through list comprehension and its built-in `str` and `int` functions. 

This ensures the resulting solution is a concise and readable one-liner, adhering to the spirit of Python's "Beautiful Soup" principle.