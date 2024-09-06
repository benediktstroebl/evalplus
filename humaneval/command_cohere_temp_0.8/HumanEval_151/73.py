```python
def double_the_difference(lst):
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result
```
The code uses a for loop to iterate through each number in the input list `lst`. It only adds the number to the `result` if it is a positive integer. If a number meets these conditions, it is squared and added to the `result`. This approach takes care of the outlined scenarios in the problem statement, including handling an empty list, so the function will return 0 in such a case.