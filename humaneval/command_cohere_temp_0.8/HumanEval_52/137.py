```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the built-in `all` function to iterate over all elements in the input list `l` and checks if all elements are less than the given threshold `t`. 

Such a solution takes advantage of the short-circuit evaluation of the `all` function. When the first “bad” element that is not less than the threshold is encountered, the `all` function stops checking and returns `False`. Thus, it is not necessary to iterate over the entire list when the first “bad” element is found.

The function header matches the problem statement, taking a list l and an integer t as input and returning a boolean indicating whether all numbers in l are below threshold t.

This solution is concise and efficient, capable of handling the specified test cases and delivering the expected functionality.