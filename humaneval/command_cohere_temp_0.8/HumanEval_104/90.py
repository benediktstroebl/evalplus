```python
def unique_digits(xs):
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)
```
The function unique_digits(xs) takes a list of positive integers, xs, as its input. It uses a list comprehension to filter out elements that have at least one even digit when converted to a string and converted back to an integer with int(y). The str(x) method is used to convert each element x to a string, and the int(y) function is used to convert each digit y back to an integer. The expression int(y) % 2 == 0 checks if the digit y is even. The any function is used to determine if any of the digits in the string representation of x have the property that int(y) % 2 == 0 is True, indicating the presence of an even digit.

The resulting filtered list is then sorted in increasing order using the sorted function and returned as the output.