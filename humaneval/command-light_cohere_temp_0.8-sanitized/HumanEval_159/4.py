def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.

    If:
        if there are not enough remaining carrots, you will eat all remaining carrots.
    return:
        [ total number of eaten carrots after meals,
        the number of carrots left after meals ]

    Const:
    number <= 1000
    need <= 1000
    remaining <= 1000

    """
    if number > remaining or need > 1000:
        return [0, 0]

    eaten = number + need
    remaining_to_eat = remaining - eaten

    return [eaten, remaining_to_eat]