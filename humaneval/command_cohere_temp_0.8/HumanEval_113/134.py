```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, d)))) for d in lst]
    return ["the number of odd elements in the string %s of the input." % i for i in r]
```

Here's a breakdown of the code:
- The `odd_count` function takes a list of lists as input.
- For each list `d` in the input, it calculates the length of a filtered list where every digit `d` is checked if it's odd, using the filter and lambda functions.
- Each filtered list is converted to a string, and these strings are stored in a new list called `r`.
- The `r` list is then formatted with the corresponding string replacements to achieve the desired output format, and returned. 

This solution is efficient and adheres closely to the provided test cases and problem statement. Let me know if further clarification is needed.