Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ng, nm = 0, 0
    if n+need > rem:
        ng = n+need
        nm = rem
    else:
        ng = n+need
        nm = n
    return [ng, nm]
```
This script defines a Python function called 'eat' that takes three parameters: 'n', 'need', and 'rem'. The function calculates the number of carrots the rabbit can eat and the number of carrots remaining after eating. 

It assigns the initial values of 0 to the variables 'ng' and 'nm' respectively. If the sum of eaten carrots ('n') and the required carrots ('need') is greater than the total remaining carrots ('rem'), it eats the total remaining carrots and updates the number of remaining carrots to zero. Otherwise, it eats the needed number of carrots and updates the remaining carrots to the previous eaten carrots number. 

Finally, the function returns a list containing [ng, nm], which represents the total number of eaten carrots after meals and the number of carrots left after meals respectively.