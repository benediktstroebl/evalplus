
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

    # Calculate the number of remaining carrots
    remaining_carrots = remaining // 5

    # Calculate the number of meals needed
    meals_needed = need // 5

    # Eat the number of carrots needed
    num_carrots_eaten = number + meals_needed

    # Calculate the total number of remaining carrots
    total_remaining_carrots = remaining - meals_needed * 5

    # Print the result
    print("[", num_carrots_eaten, "]")
    print("[", total_remaining_carrots, "]")

    return [num_carrots_eaten, total_remaining_carrots]