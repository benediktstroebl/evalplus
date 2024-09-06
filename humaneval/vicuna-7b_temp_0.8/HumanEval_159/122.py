
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
    # 找到我需要吃的总数，不吃的总数
    num_to_eat = need - number
    remaining_to_eat = remaining - num_to_eat
    
    # 如果没有剩余的關稅，就吃完所有關稅
    if remaining_to_eat == 0:
        eaten_num = need
        remaining = 0
    else:
        # 如果需要吃的总数不足，就吃整個關稅
        eaten_num = number
        remaining = 0
    return [eaten_num, remaining]

