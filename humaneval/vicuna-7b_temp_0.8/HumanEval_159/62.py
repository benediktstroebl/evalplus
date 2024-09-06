
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
    # 获取所有已经吃的肉末数
    eaten_carrots = number - remaining
    # 获取需要吃的肉末数
    remaining_carrots = need - remaining
    # 计算已经吃完的肉末数和余下的肉末数
    total_eaten_carrots = eaten_carrots + remaining_carrops
    if total_eaten_carrots > remaining_carrops:
        print("You have eaten all remaining carrots, but still hungry")
        return [0, 0]
    return [total_eaten_carrots, remaining_carrops]

