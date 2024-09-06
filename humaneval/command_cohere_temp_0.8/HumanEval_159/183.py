Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct = n + need
    if ct > rem:
        ct = rem
    return [ct, rem-ct]
```
This function takes in 3 parameters, namely `n` which represents the number of carrots already eaten, `need` which represents the number of carrots needed to be eaten, and `rem` which represents the remaining number of carrots. The function calculates the total number of carrots needed to be eaten (`ct`) based on the given constraints and returns a list containing `[ct, rem-ct]` after eating the necessary amount. 

Here is an example usage of the function:
```python
eat(2, 7, 10) # Output: [9, 1]
```
This calls the function with the arguments of already eaten carrots as `2`, the number of carrots needed to be eaten `7`, and the remaining carrots `10`. The function returns the list `[[9, 1]]` which indicates that after eating the necessary carrots, there are 9 carrots left to be eaten and 1 remaining carrot after that. 

This script will provide the output as shown in the example usage for any valid input to the `eat` function, with the constraints provided.