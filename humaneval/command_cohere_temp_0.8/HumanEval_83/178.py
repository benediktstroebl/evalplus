```python
def starts_one_ends(n):
    return sum(map(lambda x: 1 if x[0] == '1' or x[-1] == '1' else 0,
                      itertools.combinations(range(10**n), n)))
```
This function uses a combination of ranged integers and iterates through them, checking for the first or last digit to be a 1, and assigns 1 to the count if true or 0 if false, and then sums up the counts returning the result. 

This should return the required answer for the given problem. Let me know if you'd like me to break down the solution further, or elaborate on any of the steps taken to arrive at it!