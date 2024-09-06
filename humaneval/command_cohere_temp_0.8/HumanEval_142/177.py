```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

This script defines a function called `sum_squares` taking a list of integers as an input parameter `lst`. This function calculates the sum of squares for integer entries if their index is a multiple of 3 and the sum of cubes for integer entries if their index is a multiple of 4 but not a multiple of 3. The script then returns the calculated sum. 

The `enumerate` loop is used to iterate over each entry in the input list `lst`. The `if` and `elif` statements handle the conditions required for squaring or cubing the entries. The `result` variable is incremented each time with the squared or cubed value of the integer entry.

This solution is efficient and uses a single loop to iterate through the list. It utilizes the `enumerate` function to simplify the indexing and calculation process while using a single `result` variable to store the sum of the squared or cubed values.