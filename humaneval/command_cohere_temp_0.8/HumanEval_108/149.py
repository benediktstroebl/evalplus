```python
def count_nums(arr):
    return sum(x > 0 for x in map(sum, map(int, str(n)) for n in arr))
```
The function uses two levels of map operation, first, it maps int(str(n)) which converts the integer n into its integer representation, then it maps sum function to convert the integer into a single digit integer, which can be used for the comparison. The code then returns the count of elements with a digit sum > 0.