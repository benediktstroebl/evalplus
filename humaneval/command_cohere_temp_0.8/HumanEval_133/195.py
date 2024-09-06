```python
def sum_squares(lst):
    result = 0
    for n in lst:
        result += n**2
    return int(result)
```

The function **sum_squares** takes a list of numbers (*lst*) as an input, it squares each number in the list using a for loop, then it returns the sum of the squared numbers, lastly, it converts the answer to the smallest upper integer, which is the expected output format. 

This solution should work correctly for the problem statement provided.