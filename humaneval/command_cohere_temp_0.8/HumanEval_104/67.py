```python
def unique_digits(xs):
    odd = [x for x in xs if any(int(y) % 2 != 0 for y in str(x))]
    return sorted(odd)
```
```
The function unique_digits(xs) takes a list of integers xs as input and returns a sorted list of elements that contain no even digits. The function initially iterates over the list of integers xs using a list comprehension. It verifies each integer x by examining each digit in the string representation of x using the any function in conjunction with a conditional expression int(y) % 2 != 0. This verifies if any of the digits have an odd value. 

Elements with at least one odd digit will be included in the odd list if this condition is satisfied. The function then sorts the odd list in ascending order and returns the final result.
```