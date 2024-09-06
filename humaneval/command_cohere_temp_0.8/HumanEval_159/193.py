Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    total, remaining = n, rem
    if need > remaining:
        total = remaining
    elif need > 0:
        total, remaining = total + need, remaining - need
    return [total, remaining]
```
This function takes in 3 parameters, namely `n` which represents the number of carrots already eaten, `need` which represents the more carrots needed to be eaten, and `rem` which represents the remaining carrots available. The function updates the `total` and `remaining` variables and returns a list containing the number of carrots eaten and the number of carrots left. 

Here is an example usage of the function:
```python
print(eat(5, 6, 10))
```
This would print out the following output:
```
[11, 4]
```

This demonstrates the function correctly calculating the number of carrots eaten and remaining after meals considering the provided constraints. 
If you have any questions or need further assistance, feel free to ask!