```python
def odd_count(strings):
    r = []
    for string in strings:
        # split string into list of digits
        d = list(string)
        # count odd digits
        n = sum(1 for x in d if x % 2 == 1)
        # format result
        r.append(f"the number of odd elements in the string {n} of the input.")
    return r
```

Here is a concise version using Python's expression syntax:
```python
def odd_count(strings):
    return [f"the number of odd elements in the string {sum(x % 2 == 1 for x in s)} of the input." for s in strings]
```

Both scripts produce the same outputs for the test cases provided in the markdown code block and thus yield the same passes/failures for the specified tests.

The concise version leverages Python's list comprehension and expression syntax to achieve the same outcome in a more compact form. 

These scripts assume that the input list of strings contains only digits and will fail if non-digit characters are present.