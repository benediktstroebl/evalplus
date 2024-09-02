
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
    # get the modulo of the two numbers
    # the modulo is the number that should be removed when we subtract
    # these two numbers
    modulo = number % need
    
    # we don't need to eat the modulo, so we substract the modulo from
    # the need
    need -= modulo
    
    # the number of needed carrots will give us the number of remaining
    # carrots.
    needed_carrots = need
    
    # we can now eat this many carrots
    extra_carrots = math.ceil(needed_carrots / remaining)
    
    # we can now eat this many additional carrots
    extra_carrots += number - extra_carrots * remaining

    return [needed_carrots + extra_carrots, number - extra_carrots]
