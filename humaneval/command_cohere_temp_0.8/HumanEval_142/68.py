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
The function sums over the list, updating each element in-place if the index criteria are met, and returns the total. The `enumerate` loop helps track the index and value. 

You can test this code by calling the function with a list of inputs, such as `sum_squares([1, 2, 3, 4, 5, 6])`, to verify the results against the examples provided.