
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
    if remaining == 0:
        return [0, 0]
    if need <= 0:
        return [0, 0]
    
    carrots_eaten = [number] + [int(x) for x in str(number)]
    remaining_carrots = int(remaining)
    
    for i in range(1, len(carrots_eaten)):
        if carrots_eaten[i] > 0:
            if carrots_eaten[i] >= remaining_carrots:
                carrots_eaten.remove(carrots_eaten[i])
                remaining_carrots -= 1
            else:
                carrots_eaten.remove(carrots_eaten[i])
                remaining_carrots -= carrots_eaten[i]
                if remaining_carrots == 0:
                    return [0, 0]
    
    return [remaining_carrots, 0]