
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
    # move all the constraints
    number -= 1
    need -= 1
    remaining -= 1
    
    # while the number of eaten carrots < the number of needed carrots
    while number > 0 and need > 0:
        # if there are enough remaining carrots to fulfill the need
        if remaining >= need:
            # eat remaining carrots
            eaten += remaining
            remaining = 0
            need = 0
        # if not enough remaining carrots to fulfill the need
        else:
            # eat remaining carrots
            eaten += remaining
            # reset the remaining carrots to zero
            remaining = 0
            # subtract the eaten carrots from the needed carrots
            need -= eaten
            # the number of eaten carrots will be added to the returned array
            # so we don't need to add it again
        # increase the number of eaten carrots
        number -= 1
    
    return [eaten, remaining]