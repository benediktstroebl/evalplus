Here's a Python script that contains a function eat() that solves the given problem:
```python
def eat(n, need, rem):
    # eat all needed carrots
    n, rem = n + need, rem - need
    
    # handle overshoot and return values
    if n > rem:
        n, rem = rem, 0
    return [n, rem]
```
This script defines a function 'eat' that takes three parameters: 'number', 'need' and 'remaining'. It ensures that the rabbit eats the required number of carrots, subtracts this amount from the total eaten carrots and remaining carrots, and then handles overshoot scenarios by eating only the available amount of carrots, while reflecting this in the remaining parameters. 

The function returns a list containing the total number of carrots eaten after the meals and the number of carrots left after the rabbit's meals.