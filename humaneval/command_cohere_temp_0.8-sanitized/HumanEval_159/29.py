def eat(n, need, rem):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    """
    eat_amount = max(0, min(need, rem))  # eat as much as you can, but not more than need or than you have
    n, rem = n + eat_amount, rem - eat_amount  # update current state
    return [n, rem]