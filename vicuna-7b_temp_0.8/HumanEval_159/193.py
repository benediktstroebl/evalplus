
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    # your current level of hunger
    hungry = 100 - number
    # your current level of satisfaction
    satisfaction = number

    # the number of carrots that you have eaten
    num_eaten = 0

    # the number of carrots that you need to eat
    num_remaining = need - remaining

    # while you're not satisfied and there are enough remaining carrots
    while hungry > 0 and num_remaining > 0:
        # eat as many carrots as you can
        num_eaten = min(remaining, num_remaining)
        num_eaten += 1
        satisfaction += num_remaining
        num_remaining -= num_remaining

        # update the number of remaining carrots
        remaining = remaining - num_eaten

        # update the number of carrots you need to eat
        num_remaining = num_remaining - num_eaten

    # update the number of carrots you've eaten
    num_eaten = max(num_eaten, 0)

    # return the total number of carrots you've eaten
    return [num_eaten, satisfaction]