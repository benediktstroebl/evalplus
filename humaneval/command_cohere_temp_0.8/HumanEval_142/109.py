```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num **= 2
        elif i % 4 == 0 and i % 3 != 0:
            num **= 3
        result += num
    return result
```

The script uses a for loop to iterate through each index and corresponding value in the provided list. The `enumerate` function is used to access the index (`i`) and value (`num`) of each list element. Using the modulo operator (`%`), it checks whether the index is a multiple of 3 or 4.

For indices that are a multiple of 3, the script squares the integer entry. For indices that are a multiple of 4 but not a multiple of 3, the script cubes the integer entry. The sum of all entries is then returned at the end.

This script addresses the problem in a straightforward manner and produces the required result, consequently, it also passes the tests outlined in the prompt.