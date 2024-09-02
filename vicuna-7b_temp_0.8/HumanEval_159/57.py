
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

    # 讀取剩餘的藥水點數
    remaining_carrots = remaining // 5

    # 回調初始數
    number += 1
    need -= 1
    remaining -= remaining_carrots

    # 創建一個列表
    eaten = [0] * 1000

    while remaining > 0:
        # 找到最大的一個距離，並創建一個空白的字典
        max_distance = remaining_carrots
        distance_dict = {}

        for i in range(max_distance):
            # 尋找一個能夠滿足需求的距離
            if eaten[-1 - i] == 0:
                remaining_carrots = max_distance - i - 1
                break
            else:
                remaining_carrots = max_distance - i

            # 將這個距離加入字典中
            distance_dict[i] = remaining_carrots

        # 更新最後一個發現的距離
        max_distance = distance_dict.keys()[0] + 1

        # 回調需求
        need = max_distance - 1

        # 回調剩餘
        remaining = remaining_carrots

        # 發現所有可能的距離
        for i in range(max_distance):
            eaten.append(eaten[-1 - i] + 1)

        # 將最後一個發現的距離加入字典中
        distance_dict[max_distance] = remaining

    # 返回結果
    return eaten, remaining