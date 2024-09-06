```python
def unique_digits(x):
    odd = [elem for elem in x if not any(int(d) % 2 == 0 for d in str(elem))]
    return sorted(odd)
```

The function `unique_digits` uses a list comprehension that checks if any digit of the string representation of an element is even, using the `any` and `int` functions combination. The `not ` (`not any`) combination is used to return elements that shouldn't be included, i.e., elements with at least one odd digit. The function returns a sorted list of these odd-digit-including elements.