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
The function sums over the list and for each entry it determines whether its index is a multiple of 3 or 4, then squares or cuboids the 
entry respectively. The resulting sum is then returned. The script passes the given tests of the previous task statement.