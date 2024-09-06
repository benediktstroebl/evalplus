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
This function iterates through the list, and depending on the index's divisibility, it squares or cubes the value, updating the result accordingly. Finally, it returns the calculated sum. While basic, this efficiently solves the problem. Let me know if you would like to further discuss any coding concepts!