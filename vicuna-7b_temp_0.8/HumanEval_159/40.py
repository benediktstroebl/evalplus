
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

    # if not enough remaining carrots to fulfill the need
    if remaining == 0:
        return [0, 0]

    # subtract the number of eaten carrots from the remaining
    remaining -= number

    # if there are not enough remaining carrots, eat all remaining carrots
    if remaining == 0:
        return [0, 0]

    # if the number of eaten carrots is less than the need, return the number of remaining carrots
    if number + remaining <= need:
        return [number + remaining, 0]

    # otherwise, subtract the number of remaining carrots from the number of eaten carrots
    # and return the number of remaining carrots
    else:
        return [number, remaining]