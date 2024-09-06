Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    eat_all = True if need > rem else False
    if eat_all:
        return [n + rem, 0]
    else:
        return [n + need, rem - need]
```
This script and function work correctly for the given problem constraints, including edge cases.