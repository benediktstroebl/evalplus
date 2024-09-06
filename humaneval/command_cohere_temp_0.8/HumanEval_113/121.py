```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for c in digits if c % 2 != 0))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This code solves the problem by using a sum function in conjunction with a generator expression to count the number of odd digits in each string in the list `lst`. The result is a list of strings describing the number of odd elements in each string of the input. 

To execute the tests for this code you can call the `odd_count` function with the test inputs described in the problem, and compare the resulting output against the expected output with an appropriate assert statement.