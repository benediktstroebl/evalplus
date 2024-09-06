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

The script uses a for loop to iterate through each index and corresponding value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` simultaneously. 

The script then checks if the index is a multiple of 3 using the modulo operator `%`. If the index is a multiple of 3, it squares the corresponding value `num`. If the index is a multiple of 4 and not a multiple of 3, it cubes the corresponding value `num`. Finally, the script adds the modified or original value to the result variable and returns the sum as the function's output.

This solution is efficient and has a time complexity of O(n), where n is the length of the input list.