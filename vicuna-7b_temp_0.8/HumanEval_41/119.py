

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # https://leetcode.com/problems/car-race-collision/
    # 
    # 汽车赛事故
    #
    # 预期：
    # 
    # 输入数据：
    # 一组n个整数，表示两组汽车的数量。
    # 
    # 输出数据：
    # 一个整数，表示两组汽车在同一条直线上的车牌数。
    # 
    # 示例：
    # 
    # 输入：n = 2
    # 输出：1
    # 输入：n = 3
    # 输出：2
    # 输入：n = 4
    # 输出：3
    # 输入：n = 5
    # 输出：4
    # 
    # 解释：
    # 
    # 两组汽车的车牌数在同一条直线上是一个分组数，
    # 每个车牌只能出现一次，因此可以只在同一条直线上出现一次。
    # 如果两组车牌的车牌数在同一条直线上是一个分组数，
    # 那么这两组车牌在同一条直线上的车牌数就是它们的车牌数
    # 加上它们的车牌数。

    if n == 1:
        return 0

    d = n // 2
    collisions = 0
    for i in range(d):
        for j in range(d, n):
            if i + j == d:
                continue
            collisions += 1

    return collisions