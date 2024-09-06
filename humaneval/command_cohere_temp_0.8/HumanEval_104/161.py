```python
def unique_digits(xs):
    odd_digits = [int(''.join(x for x in str(n) if x.isdigit() and x % 2 != 0)) for n in xs]
    return sorted(odd_digits)
```

The function `unique_digits` takes a list of positive integers (`xs`) as input and returns a sorted list of all elements that contain no even digits. It does so by converting each number to a string, filtering out odd digits, converting them back to integers, and storing them in the `odd_digits` list. Ultimately, it sorts that list and returns the result. 

This solution does not require any additional modules and adheres to the problem's given requirements.