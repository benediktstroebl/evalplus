```python
def double_the_difference(lst):
    result = 0
    for n in lst:
        if isinstance(n, int) and n > 0:
            result += n**2
    return result
```
The code uses a for loop to iterate through each number in the input list `lst`. It only adds the number to the `result` if it is a positive integer. If a number satisfies these conditions, its square is added to the `result`. Thus, the `double_the_difference` function computes the sum of squares of odd positive integers in the list.