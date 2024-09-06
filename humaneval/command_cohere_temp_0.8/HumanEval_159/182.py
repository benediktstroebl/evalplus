Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ate = n
    if need > rem:
        ate = rem
    else:
        ate += need
    return [ate, rem-ate]
```

This function takes in three variables; `n` which represents the number of carrots already eaten, `need` which represents the additional number of carrots needed to be eaten, and `rem` which represents the remaining quantity of carrots available. 

The function returns a list containing two values: the total number of carrots eaten (which is the sum of the initial eaten carrots and the newly eaten carrots to meet the need) and the number of carrots remaining after the rabbit has eaten to fulfill its appetite. 

The function includes a check to ensure the remaining carrots in supply are sufficient to meet the required intake. If they are not, the rabbit will eat the entire remaining supply but will still be hungry as it needs more carrots going forward. This checks against the constraint provided in the prompt that stated:
```
* if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
``` 

This function addresses the main task of calculating the total eaten carrots and the remaining carrots in a self-contained manner. It also adheres to the constraints provided in the prompt with respect to input variable ranges. 

Let me know if you would like me to run some test cases through this function to ensure it operates correctly.