def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    You:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number: integer, represents the number of carrots that the rabbit has eaten
    @need: integer, represents the number of carrots that the rabbit needs to eat
    @remaining: integer, represents the number of carrots left in stock after the rabbit has eaten some

    Constraints:
    @number <= 1000
    @need <= 1000
    @remaining <= 1000

    Returns:
    @total_eaten: array(int), the total number of carrots the rabbit has eaten after meals.
    @left_ carrots: array(int), the number of carrots left after meals are completed
    """
    total_eaten = number + need
    left_carrots = remaining
    return [total_eaten, left_carrots]