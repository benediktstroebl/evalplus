
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
    # Move your head to the start of the list
    for i in range(1, len(remaining)):
        remaining[i] = remaining[i-1]
        
    # Initialize number of carrots eaten and number of carrots left
    number_eaten = 0
    number_left = remaining
    
    # find the last non-negative number in remaining
    while remaining[0] >= 0:
        remaining.pop(0)
        number_eaten += remaining.pop(0)
    number_eaten += remaining.pop(0)
    
    # move number_eaten to end of list
    for i in range(1, len(number_eaten)):
        number_eaten[i] = number_eaten[i-1]
    
    # return the total number of eaten carrots and the number of carrots left
    return number_eaten, number_left