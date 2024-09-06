```python
def number_of_odd(lst):
    r = []
    for x in lst:
        o = sum(1 for i in x if i % 2 != 0)
        r += [f"the number of odd elements {o} in the string {x} of the input"]
    return r
```

The function `number_of_odd` employs a generator expression within a loop to tally the odd digits in each string of the input list, crafting a corresponding list of descriptors. 

The `odd_count` tests, provided in the original prompt, are suited for this solution and can be added to validate the function.