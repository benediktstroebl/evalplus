
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
    # 计算需要吃的数量
    days = int(number / 100)
    remaining_num = number % 100
    need_num = int(need)
    # 计算剩余数量
    remaining = remaining_num
    total_num = 0
    while remaining > 0:
        # 吃一顿，把数量减去
        total_num += 100
        remaining = remaining // 100
        if remaining == 0:
            break
    # 将剩余数量添加到需要吃的数量中
    need_num += remaining
    # 将吃完毕的数量加到total_num中
    total_num += days
    # 将每天的数量合并成一个数组
    day_nums = [total_num]
    for i in range(1, days + 1):
        if i % 100 == 0:
            day_nums.append(day_nums[-1] * 100)
    # 将每天的数量添加到需要吃的数量中
    need_num = need_num * days
    for i in range(1, days + 1):
        if need_num >= day_nums[i]:
            need_num -= day_nums[i]
        else:
            need_num = 0
    # 返回结果
    return [total_num, remaining]