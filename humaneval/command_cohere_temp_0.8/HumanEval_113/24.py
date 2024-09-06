```python
def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for c in digits if c % 2 != 0))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r
```

This solution uses a simple loop to iterate through each string in the list and calculate the count of odd digits in each string. The count is appended to a sentence as an integer, resulting in a list of formatted strings that answer the question for each input string. The solution is encapsulated in the `odd_count` function, which provides the output as a list of strings.