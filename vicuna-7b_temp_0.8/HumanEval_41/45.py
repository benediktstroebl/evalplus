

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
    # 将车辆的速度存储在一个列表中，每一行包含一个车辆的速度
    car_speeds = [f"{i+1}km/h" for i in range(n)]

    # 遍历每一行，查找车辆在左向右行走的车辆和右向左行走的车辆
    for i in range(n-1):
        if car_speeds[i] > car_speeds[i+1]:
            # 如果车辆在左向右行走的速度比右向左行走的速度更快，则说明这两个车辆会相互衝突
            print(i+1)

    # 输出结果
    print(n-1)
