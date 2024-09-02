

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
    # SOLUTION: 4
    # 1. n=2
    # 2. n=3
    # 3. n=4
    # 4. n=5
    # 5. n=6
    # 6. n=7
    # ...
    # 20. n=1
    # 21. n=2
    # 22. n=3
    # 23. n=4
    # ...
    # 100. n=9
    # 101. n=10
    # ...
    # 1000. n=1
    # 1001. n=2
    # ...
    # 10000. n=9
    # 10001. n=10
    # ...
    # 100000. n=1
    # ...
    
    for i in range(n):
        for j in range(n):
            if (i+1) % 2 == 0 or (i-1) % 2 == 0 or (j+1) % 2 == 0 or (j-1) % 2 == 0:
                continue
            if i == j:
                continue
            #print(i, j, i+1, j+1)
            # 2. n=3
            # 3. n=4
            # ...
            # 10. n=9
            # 11. n=10
            # ...
            # 100. n=9
            # 101. n=10
            # ...
            # 1000. n=1
            # 1001. n=2
            # ...
            # 10000. n=9
            # 10001. n=10
            # ...
            # 100000. n=1
    return 0
