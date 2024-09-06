```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This solution uses the built-in Python functionality to split the string 's' at the 'and' delimiter, which creates the list ['apples', 'oranges']. Then, using the map() function, it converts these elements into integers I then subtract these quantities from the total number of fruits to find the number of mangoes. This performs the intended calculation of the number of mangoes in the basket.