
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

    # Check if you have enough remaining carrots
    if remaining == 0:
        # If you don't, eat all remaining carrots
        print("You are still hungry")
        return [remaining, 0]

    # Calculate the number of carrots you need to eat
    num_to_eat = min(need - number, remaining)

    # Calculate the number of carrots you have eaten
    num_eaten = number + num_to_eat

    # Calculate the remaining number of carrots after your meals
    remaining_carrots = remaining - num_to_eat

    return [num_eaten, remaining_carrots]