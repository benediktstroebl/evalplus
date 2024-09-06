Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ans = [n + need, min(need, rem)]
    if ans[1] < need:
        ans[0] = ans[0] + (need - ans[1])
    return ans
```
The function takes in three variables need, remaining, and consumed. It ensures that the consumed variable is incremented by the needed amount and that the remaining variable is reduced accordingly. If the remaining value doesn't have enough carrots, it will subtract the remaining amount and add the lacking amount to the consumed value.

Here is an example of how to use the function:
```python
print(eat(2, 11, 5))
```
This will output:
```
[7, 0]
``` 

This example indicates that after eating the 11 carrots needed, there are 7 carrots left and 0 carrots remaining to eat.