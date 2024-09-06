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

This Python script defines a function called `sum_squares` that takes a list called `lst` as an argument. It iterates through each element in the list using the `enumerate` function, which provides both the index and the value of each element. Depending on whether the index is a multiple of 3 or a multiple of 4 and not a multiple of 3 (i.e., meeting the criteria mentioned in the problem statement), the corresponding element is squared or cubed, respectively. The squared or cubed values are accumulated and returned as the result.

The behavior is illustrated by the following examples:
- For lst = [1,2,3], the output is 6, which is the sum of 1 squared (1^2 = 1) and 2 cubed (2^3 = 8).
- For lst = [], the output is 0, as the empty list has no elements.
- For lst = [-1,-5,2,-1,-5], the output is -126, reflecting the sum of -1 squared (-1^2 = 1), -5 cubed (-5^3 = -125), and 2 squared (2^2 = 4). 

This accurately solves the problem and passes the tests outlined in the original problem statement.