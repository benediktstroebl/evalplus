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
The code uses a for loop to iterate through each index and value in the input list `lst`. The `enumerate` function is used to access the index `i` and the value `num` of the list element simultaneously.

For each element, the code checks the index modulo 3 and 4 to determine whether it should square or cube the element. It accumulates the sum of all modified elements into the variable `result` and finally returns that value. 

This solution fulfills the problem statement while staying under the 100 lines of code threshold. Let me know if it works correctly!