
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

    # If the number of carrots eaten is more than the carrots required to be eaten, 
    # we need to take the difference and keep the remaining carrots
    # For example: number = 7 and need = 6. Then we can eat 1 extra carrot
    # so we need to subtract the difference.
    # So the number of carrots to be eaten is 6 and remaining carrots is 1
    if number > need:
        number -= (number - need)
        remaining = number - need
    
    # If the number of carrots eaten is more than the number of carrots that are left,
    # then we have eaten all the carrots. So we will have zero remaining carrots.
    if number > remaining:
        remaining = 0
    
    # If the number of carrots eaten is less than the number of carrots that are left,
    # then the number of carrots left is the difference between the number of carrots
    # eaten and the number of carrots that are left.
    if number < remaining:
        remaining = number - remaining
    
    # Here we return the result as an array
    return [number + need, remaining]
