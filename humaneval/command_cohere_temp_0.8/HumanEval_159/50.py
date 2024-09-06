Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    eatsome = min(need, rem)
    n += eatsome
    rem -= eatsome
    return [n, rem]
```
This function uses three parameters: `n` which represents the number of carrots already eaten, `need` which represents the additional number of carrots needed to be eaten, and `rem` which represents the remaining quantity of carrots available. The function returns a list containing two pieces of information: the total number of carrots consumed in this round of eating (which is the minimum of `need` and `rem`), and the number of carrots remaining after this round of eating. These values are stored in the list returned by the function as `[n, rem]`. 

Here is an example usage of this function:
```python
eat(5, 6, 10)  # -> [11, 4]
```

This function adheres to the specified constraints.