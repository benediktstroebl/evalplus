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