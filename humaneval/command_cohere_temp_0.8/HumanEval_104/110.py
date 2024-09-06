```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers as input and returns a sorted list of elements that contain no even digits. The function examines each element x in the input list using a generator expression that checks if any digit in the string representation of the number is even (using the expression int(y) % 2 == 0 for y in str(x)) and if so, the element is included in the result list. The generated list is then sorted in increasing order and returned as the solution.