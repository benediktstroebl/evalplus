

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
    total = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and (i > j):
                road_1 = []
                road_2 = []
                for k in range(1, i+1):
                    road_1.append((k, 1))
                for k in range(i, n+1):
                    road_1.append((k, -1))
                for k in range(1, j+1):
                    road_2.append((k, 1))
                for k in range(j, n+1):
                    road_2.append((k, -1))
                a = 0
                while a < len(road_1):
                    if road_1[a][1] == -1 and road_2[a][1] == 1:
                        total += 1
                    a += 1
    return total
