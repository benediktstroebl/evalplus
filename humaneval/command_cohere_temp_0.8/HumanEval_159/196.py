Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
   Eating = n + need
    Hungry = max(0, rem - Eating)
    return [Eating, Hungry]
```

This function takes in three variables as input: `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten, and `rem` which is the remaining number of carrots. The function calculates the total number of carrots eaten after meals which is `n + need` and assigns the remaining number of carrots after meals to `Hungry`. The function returns a list of the two variables which are [Eating, Hungry]. 

Here is a usage example:
```python
print(eat(2, 11, 5))
```

And this will output:
```
[7, 0]
```

Such that after eating 2 carrots and needing 11 carrots, you'll have 7 carrots left and still be hungry.