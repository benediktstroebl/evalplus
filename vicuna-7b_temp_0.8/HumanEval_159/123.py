
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
    # 遍歷所有可能的解
    solutions = [(0, 0)]
    while solutions:
        # 取出前一次解
        current_solutions = solutions[1:]
        # 取出最佳解
        current_best = current_solutions[0]
        for i in range(1, len(current_solutions)):
            # 如果更好
            if current_best[1] != 0 and current_solutions[i][1] > current_best[1]:
                # 更新最佳解
                current_best = (current_best[0] + current_solutions[i][0], current_best[1] - current_solutions[i][1])
        # 剩下的余次数
        remaining_left = remaining
        # 剩下的需要吃的总量
        left_to_eat = need - current_best[0]
        # 如果剩下的余次数不足，直接将其全部吃
        while remaining_left < need and solutions:
            solutions.append((current_best[0] + remaining_left, 0))
            remaining_left -= current_best[0]
            remaining -= current_best[0]
        # 最后剩下的余次数
        remaining_left = remaining - current_best[0]
        # 剩下的需要吃的总量
        left_to_eat = need - current_best[0]
        # 将其加入前一次解中
        solutions.append((current_best[0] + remaining_left, left_to_eat))
        remaining_left = remaining
        current_best = solutions[-1]
    # 返回最佳解
    return current_best