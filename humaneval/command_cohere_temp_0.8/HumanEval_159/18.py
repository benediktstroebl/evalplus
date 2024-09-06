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
    ate = n
    if need > rem:
        (ate, rem) = (rem, 0)
    elif need < rem:
        ate += need
    total_eat = n + ate
    return [total_eat, rem]
```

This function takes in three parameters: `n` (the number of carrots already eaten), `need` (the number of carrots needed to be eaten right now), and `rem` (the number of remaining carrots). The function first sets the `ate` variable to the value of `n` which is the initial amount of carrots eaten, then we check if `need` is greater than `rem`. If it is, then the rabbit eats all the remaining carrots which might not be enough to fulfill his hunger which means the amount eaten is set to the value of `rem` and the remaining carrots are zero. If neither of these are true, then the rabbit eats the required amount of carrots to fulfill his hunger and these carrots are added to the `ate` variable. The function then returns a list containing [total eaten carrots after meals, the number of carrots left after meals].