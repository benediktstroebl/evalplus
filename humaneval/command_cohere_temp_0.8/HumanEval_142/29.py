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
The function sums over the list, computing the square if the index is a multiple of 3 and the cube if the index is a multiple of 4 and 
not a multiple of 3. The ensuing sum is then returned. The function is illustrative of basic list traversal and advanced mathematical 
operations in Python. The logic is encapsulated in a single function, achieving the desired result as outlined in the problem 
statement.