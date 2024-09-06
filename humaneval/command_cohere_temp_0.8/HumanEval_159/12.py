Here's a Python script that contains a function named `eat` which solves the given problem:
```python
def eat(n, need, rem):
   Eating = n+need
    leftover = rem-Eating
    return [Eating, leftover]
```
This function uses 3 parameters: `n` which is the number of carrots already eaten, `need` which is the number of carrots needed to be eaten right now, and `rem` which is the remaining number of carrots.

The function calculates the total eating which is the sum of already eaten carrots plus the required ones, and the leftover count which is the difference between the remaining carrots and the total eating. Both are returned as a list.

This solution goes inline with the constraint as well since the returned values are all within the specified integer ranges.