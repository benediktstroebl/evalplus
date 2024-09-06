Here's a Python script that contains a function called `eat` that solves the given problem:
```python
def eat(n, need, rem):
    """
    You're a hungry rabbit, and you already have eaten `number` of carrots,
    but now you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    If there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    eaten = n + need
    if eaten > rem:
        eaten = rem
    print(eaten)
    return [eaten, rem - eaten]
```

The function takes in three variables: `number`, `need` and `remaining` as input. It first adds the number of carrots required to the number of carrots already eaten to determine the total calories consumed by the rabbit. If the total calories consumed is greater than the number of carrots remaining, the calories consumed is set to the number of remaining carrots. 

The function then returns the variables [eaten calories, remaining carrots after consumption].

This code will output the total calories consumed by the rabbit and the number of carrots left as a list.