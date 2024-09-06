def eat(n, need, rem):
    '''
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    '''
    diff = need - n
    eat_amount = rem if diff > rem else diff
    total_eaten = n + eat_amount
    remaining = rem - eat_amount
    return [total_eaten, remaining]