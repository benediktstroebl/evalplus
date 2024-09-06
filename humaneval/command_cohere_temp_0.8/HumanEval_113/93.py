```python
def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, num))))) for num in lst]
    return ["the number of odd elements " + i + " in the string " + str(j) + " of the input." for i, j in zip(r, lst)]
```