

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
    # 输入参数
    # 首先进行处理，确定是第一个元素与第n个元素，第二个元素与第n-1个元素
    # 这样第一个元素和第n个元素是无法发生碰撞的，第二个元素和第n-1个元素也是无法发生碰撞的
    # 当然，也是有可能发生碰撞的
    # 解决方式：
    # 将第一个元素和第n个元素的结果交换，第二个元素和第n-1个元素的结果交换
    # 然后在将第一个元素和第n个元素移到最后，第二个元素和第n-1个元素移到第一个元素和第n个元素的位置
    # 以此类推
    # 每次只移动一个元素到最前面，移动后重新计算
    # 
