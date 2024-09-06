
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
    # your initial meals
    meals = [0] * 4
    
    # number of carrots you ate
    carrots_eaten = number - 500
    
    # number of carrots you need to eat
    num_to_eat = need - carrots_eaten
    
    # number of carrots left after your meals
    remaining_carrots = remaining - num_to_eat
    
    # number of meals you need to eat
    num_meals = min(4, (remaining_carrots // 500)) + 1
    
    # create a list of meals
    meals = [meals[i - 1] + 500 for i in range(num_meals)]
    
    # eat carrots
    for i in range(num_meals):
        meals[i] += 500
    
    # record the number of carrots eaten
    carrots_eaten += meals.sum()
    
    # record the number of remaining carrots
    remaining_carrots -= meals.sum()
    
    # you eat all remaining carrots
    if remaining_carrops == 0:
        remaining_carrots += meals.sum()
    
    return [carrots_eaten, remaining_carrots]