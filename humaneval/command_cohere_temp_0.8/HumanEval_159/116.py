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
This function takes in 3 parameters, namely `n` which represents the number of carrots already eaten, `need` which represents the additional carrots required, and `rem` which represents the remaining carrots available. The function calculates the total number of carrots eaten (`total`) and the number of carrots remaining (`remaining`) based on different scenarios and returns a list containing these two values.

Here is an example usage of the `eat` function:
```python
print(eat(5, 6, 10))
```
This would output:
```
[11, 4]
```

This demonstrates how the function calculates the total number of carrots eaten (11) and the remaining number of carrots (4) when the rabbit has already eaten 5 carrots, needs to eat 6 more, and has 10 carrots remaining. 

This problem can be solved using basic arithmetic and the concept of integer manipulation.