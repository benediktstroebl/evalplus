```python
def below_threshold(l, t):
    return all(x < t for x in l)
```
The function `below_threshold` uses the `all` function to check if all the numbers in the list `l` are below the threshold `t`. 

Here is an example of how to use the code:
```python
print(below_threshold([1, 2, 4, 10], 100))
print(below_threshold([1, 20, 4, 10], 5))
```
This would result in the following output:
```
True
False
```
This demonstrates that the new code still passes the given tests.