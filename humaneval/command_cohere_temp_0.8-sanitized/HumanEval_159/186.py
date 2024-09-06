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