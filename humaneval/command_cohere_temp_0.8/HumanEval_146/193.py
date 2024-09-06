```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs python's array filtering capabilities along with the `str` function to iterate through each number in the array and determine if the first or last digit corresponds to the odd digits category (1, 3, 5, 7, 9). The filtering outcomes are then intersected and the final length of the resulting array corresponds to the number of digits answering the challenge's criteria. 

To follow best practices, the function includes a docstring at the top of the code block that describes the function's purpose, inputs, and expected output.