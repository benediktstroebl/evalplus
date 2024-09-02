
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
    # 给定数量number,分配需要的数量need,剩余的数量remaining
    # 返回的数量负数表示剩余，整数表示已经跑配的，
    # 如果剩余的数量小于需要的数量，给数也变负数，表明剩余的数量可达不到需要的数量
    # 如果剩余的数量大于需要的数量，表示剩余的数量超过需要的数量
    # 例如、number = 5,need = 6,remaining = 10,返回[11,4]
    # number = 4,need = 8,remaining = 9
    # number = 1,need = 10,remaining = 10
    # number = 2,need = 11,remaining = 5
    if need <= remaining:
        return [number + need, (remaining - need)]
    elif need > remaining:
        return [number - remaining, 0]

