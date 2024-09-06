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
The code uses a for loop to iterate through each index and corresponding value in the provided list. The conditionals (`if i % 3 == 0:` and `elif i % 4 == 0 and i % 3 != 0`) manage the transformations required on each integer according to the problem description. The sum is accumulated using `result += num` and returned at the end. 

This solution allows for non-zero list indexes and manages the cases of cubes and squares as required. It adheres to Python norms and is efficient in its implementation. Let me know if you'd like to know more about the approach or the coding concepts relevant to this problem!