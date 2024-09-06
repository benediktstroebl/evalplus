```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This solution uses the built-in Python functionality to split the string into two integers. These are then subtracted from the total number of fruit to give the number of mangos. This solution does not rely on any additional libraries. 
It is also the most efficient with a time complexity of O(1) and a space complexity of O(1).