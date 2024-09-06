

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
    # 2017.12.14 スマートにカートニー単位の0から1を1まで変換する
    # カートニー単位の複数の0から1まで変換する
    # カートニー単位の1から2まで変換する
    # ...
    # カートニー単位のnから(n+1)まで変換する

    # カートニー単位の0から1までの変換を保存する
    original = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    # カートニー単位の1から2までの変換を保存する
    next = original.copy()
    next[0] = 2
    next[1] = 2

    # カートニー単位の2から3までの変換を保存する
    after = next.copy()
    after[0] = 3
    after[1] = 3

    # カートニー単位の3から4までの変換を保存する
    later = after.copy()
    later[0] = 4
    later[1] = 4

    # カートニー単位の4から5までの変換を保存する
    even_later = later.copy()
    even_later[0] = 5
    even_later[1] = 5

    # カートニー単位の5から6までの変��
