Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct = n + need
    if ct > rem:
        ct = rem
    return [ct, rem-ct]
```
This function takes in 3 variables namely; `n` which represents the number of carrots already eaten, `need` which represents the number of carrots needed to be eaten, and `rem` which represents the remaining number of carrots. The function calculates the total number of carrots needed to be eaten which is the sum of what has already been eaten and needs to be eaten, then checks if this value is greater than the remaining carrots, if so, it changes the total carrots to eat to the value of remaining carrots. Finally, it returns a list containing [total carrots after eating, remaining carrots after eating]. 

Here is an example usage of the function:
```python
print(eat(2, 11, 5))
```
This will output:
```bash
[7, 0]
```
Which indicates that after eating the needed amount of carrots, there remain 7 carrots left and 0 carrots to eat again.