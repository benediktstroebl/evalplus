
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
    # get the total number of remaining carrots
    remaining_carrots = remaining
    # count the number of carrots you ate
    ate = 0
    # check if you have eaten enough carrots
    while remaining_carrots >= need:
        ate += 1
        remaining_carrots -= 1
        if remaining_carrots == 0:
            break
    # calculate the total number of eaten carrots
    total_eaten = ate
    # calculate the number of remaining carrots
    if remaining_carrops >= 0:
        remaining_carrops += total_eaten
    else:
        remaining_carrops = 0
    return [total_eaten, remaining_carrots]

