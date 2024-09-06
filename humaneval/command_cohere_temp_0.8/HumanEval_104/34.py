```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers, xs, as input. It uses a list comprehension to filter out elements that have at least one even digit when converted to a string and converted back to an integer with int(y). The list comprehension iterates over each element x in the input list xs. For each x, it checks if any character in the string representation of x has an even digit when converted to an integer using the modulo operator (%) to check if an integer is even or not.

The resulting filtered list of elements having no even digits is then sorted in ascending order using the sorted() function and returned as the output.