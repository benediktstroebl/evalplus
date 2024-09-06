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
This script defines a Python function called 'eat' that takes three parameters: 'n', 'need', and 'rem'. This function aims to return a list containing two integers, which are the total number of carrots eaten after meals and the number of carrots left after meals, respectively.

To achieve this, the function first initializes two variables 'ng' and 'nm' to zero. Then, it checks if the sum of the number of carrots already eaten 'n' and the number of carrots needed to be eaten 'need' is greater than the remaining number of carrots 'rem'. If this condition is true, it means not enough carrots remain to meet the rabbit's dietary needs. In this case, the function sets 'ng' to the sum of 'n' and 'need', while 'nm' is set to the remaining number of carrots 'rem'. This ensures that the rabbit eats all the remaining carrots, but still feels hungry because there isn't enough food.

If the above condition is false, it means there are enough carrots to meet the rabbit's needs. In this scenario, 'ng' is set to the sum of 'n' and 'need', and 'nm' is set to the number of carrots already eaten, 'n'. This means the rabbit has eaten enough and there are still some remaining carrots left.

Finally, the function returns a list containing [ng, nm], which stands for the total number of carrots eaten after meals and the number of carrots left after meals, respectively.

This code adheres to the specified constraints of having all variables in the range of 0 to 1000.