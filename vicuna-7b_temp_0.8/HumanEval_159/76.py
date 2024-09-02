
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
    # Your current stock of carrots
    stock = remaining
    # Your current number of carrots eaten
    eaten = number + 1
    # Your current number of carrots to eat
    target = need
    
    # A list to store the number of carrots eaten
    eaten_list = [eaten]
    
    # Keep eating until you reach your target or run out of stock
    while stock > 0:
        # Eat the next number of carrots
        eaten_list.append(eaten)
        eaten += 1
        stock -= 1
        
        # Update your target
        target -= 1
        
        # Keep track of the number of carrots remaining
        remaining_list = [remaining]
        
        # If you have reached your target, return the number of eaten carrots and the number of remaining carrots
        if eaten == target:
            return eaten_list, remaining_list[0]
        
        # Update the list of remaining carrots
        remaining_list = remaining_list[:-1] + remaining_list[1:]
    
    # If you run out of stock before reaching your target, eat all remaining carrots and return the number of eaten carrots and the number of remaining carrots
    eaten_list.append(remaining)
    return eaten_list, remaining_list[0]
