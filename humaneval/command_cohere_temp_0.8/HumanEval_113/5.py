```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for d in digits if d % 2 == 1)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

This code solves the problem by using a generator expression to iterate over each digit in the list of strings, counting the number of odd digits, and appending a corresponding string to the result list.

To use this code simply run it and invoke the `odd_count` function with a list of digit strings as shown in the test cases above.