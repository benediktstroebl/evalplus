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

The code uses a for loop to iterate through each index `i` and corresponding value `num` in the list `lst`. The `enumerate`  technique makes code more readable and provides a clear way to understand the index and value of items in the list while it is being processed. Using the `if` and `elif` statements, the code at each iteration decides whether the current index is divisible by 3, 4, or both. The integer value is squared if the index is a multiple of 3. The integer value is cubed if the index is a multiple of 4 and not a multiple of 3. The sum is then calculated by adding the modified (or unmodified) integer value to the result variable. Ultimately, the function returns the value of the result variable, which is the sum of all list values after having been altered according to their indices. 

This code should be able to pass all test cases outlined in the problem prompt, including edge cases like empty lists and negative values, as it is designed to handle any index and value combinations that are feasible in a list.