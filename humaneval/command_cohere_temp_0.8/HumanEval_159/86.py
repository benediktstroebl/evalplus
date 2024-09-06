Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    ct = n + need
    if ct > rem:
        ct = rem
    return [ct, rem-ct]
```
This function takes in 3 parameters, namely `n` which represents the number of carrots already eaten, `need` which represents the number of carrots needed to be eaten, and `rem` which represents the remaining quantity of carrots. The function calculates the total number of carrots present and returns an array of the form `[total_eaten, remaining]`. If the total number of carrots to be eaten exceeds the remaining quantity, the total eaten quantity will be set to the remaining quantity.

Here is an example usage of the function:
```python
eat(2, 7, 10)  # Output: [9, 1]
```
This calls the `eat` function with the arguments of already eaten carrots as `2`, the required number of carrots to be eaten `7`, and the remaining quantity of carrots `10`. The function calculates the total eaten returning `[9, 1]` which means 9 carrots were eaten and 1 carrot remains.

This script should be able to pass all test cases for the given problem statement.