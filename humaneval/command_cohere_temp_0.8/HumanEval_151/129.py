```python
def double_the_difference(lst):
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2:
            result += num ** 2
    return result
```
The function `double_the_difference` iterates through each number in the input list `lst`. For each number, it checks whether it's an integer and whether it's odd (i.e., divisible by 2 but yielding a non-zero remainder). If these conditions are met, it adds the square of that number to the `result` variable. Finally, the function returns the `result`, which will be the sum of squares of all odd integers in the list.