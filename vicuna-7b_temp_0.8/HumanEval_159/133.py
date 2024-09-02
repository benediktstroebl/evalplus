
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
    # 对于第一个例子，我们需要尝尝10个甜菜，但只剩下了9个甜菜。
    # 因此我们可以尝尝所有的甜菜，但我们仍然会感到寂难。
    if need <= 0:
        return [0, 0]  # 没有剩下的甜菜，还是寂难

    # 对于第二个例子，我们需要尝尝8个甜菜，但只剩下了1个甜菜。
    # 因此我们需要尝尝所有的甜菜，但是由于我们已经没有甜菜了，因此我们仍然会感到寂难。
    # 另外，我们的体力还会下降 1，因为我们没有甜菜吃。
    if need == 0:
        return [0, 0]  # 没有剩下的甜菜，还是寂难

    # 对于第三个例子，我们需要尝尝5个甜菜，但只剩下了10个甜菜。
    # 因此我们可以尝尝所有的甜菜，但我们仍然会感到寂难。
    # 另外，我们的体力还会下降 10，因为我们没有甜菜吃。
    if need == 0:
        return [0, 0]  # 没有剩下的甜菜，还是寂难

    # 尝尝一次
    remaining_carrots = remaining
    eaten_
