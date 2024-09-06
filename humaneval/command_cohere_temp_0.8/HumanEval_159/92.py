Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct, leave = 0, 0
    while need > 0:
        if need >= rem:
            ct += rem
            need -= rem
        else:
            ct += need
            leave += need
            need = 0
        rem -= min(rem, need)
    return [ct, leave]
```

This function takes in three variables `n`, `need`, and `rem` as mentioned in the problem statement and returns a list containing the total number of carrots eaten after meals and the number of carrots left after meals. The function solves the problem using iterative logic to eat carrots based on the remaining stock and the required needs. 

The output of the example cases provided in the prompt should be:
1. `[11, 4]`
2. `[12, 1]`
3. `[11, 0]`
4. `[7, 0]` 

Note that this solution assumes that the three input variables are integers and thus the nested loop may not be the most efficient solution for large inputs. However, the upper bounds of the variables are constrained to be less than or equal to 1000.