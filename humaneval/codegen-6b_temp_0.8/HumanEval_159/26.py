
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
    if (number >= need):
        # since we know that we have enough to eat, we can immediately eat
        # all of the carrots and return our result
        return [number + need, 0]
        
    elif(need > number):
        # how many carrots we can eat is the number left over
        # if we don't have enough to eat, just eat all remaining carrots
        remaining -= number
        return [need, remaining + need]
        
    else:
        # we aren't even able to handle the extra demand
        # we'll just eat as much as we can, and return the remaining
        # number of carrots left
        return [need, remaining]

