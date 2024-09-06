Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    dist = need - n
    if dist > rem:
        dist = rem
    n += dist
    rem -= dist
    return [n, rem]
```

This function takes in three parameters: `n` which represents the number of carrots already eaten, `need` which represents the total number of carrots needed, and `rem` which represents the remaining quantity of carrots. 

The function returns a list containing two items: the total number of carrots consumed (`n`) and the number of carrots remaining (`rem`). 

It ensures that the deficit between the required and already consumed carrots doesn't exceed the total remaining quantity, and updates the total consumed and remaining quantities accordingly. 

Here is the previous response formatted as a markdown code block:
```python
def eat(n, need, rem):
    dist = need - n
    if dist > rem:
        dist = rem
    n += dist
    rem -= dist
    return [n, rem]
```
You can copy and paste this code block into a Python environment to test the function.