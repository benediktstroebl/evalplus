```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for digit in digits if digit % 2 != 0))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This solution uses a simple loop to iterate through each string in the list and calculate the number of odd digits using a generator expression. The sum of odd digits is converted to a string using `str`, and the result is formatted using an interpolation syntax to insert the count of odd digits into the string. This format is consistent with the prompt's desired output format.