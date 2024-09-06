```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the `all` function to check if all the numbers in the list `l` are below the threshold `t`. 

Here is an example of how to use the code:
```python
>>> below_threshold([1, 2, 4, 10], 100)
True
>>> below_threshold([1, 20, 4, 10], 5)
False
```

The first test case passes since all the numbers in the list `[1, 2, 4, 10]` are less than the threshold `100`. The second test case fails because the number `20` in the list is greater than the threshold `5`.