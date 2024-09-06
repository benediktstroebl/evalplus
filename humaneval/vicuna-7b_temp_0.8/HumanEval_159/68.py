
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
    # 创建一个变量 total 来记录总见萝��loped
    total = number + need
    # 如果需要的见萝��loped不为空，就遍历所有的见萝��loped
    if need != 0:
        for i in range(remaining):
            # 如果已经吃完所有见萝��loped，说明没有足够的见萝��loped
            if total - i >= 0:
                print("You are full, can't eat more carrots")
                return [total - i, 0]
            else:
                print("Eat one carrot")
                number += 1
                remaining -= 1
        # 当我们已经吃完所有见萝��loped时，