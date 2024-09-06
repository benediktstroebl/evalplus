

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
    # 1st approach: use a recursion and use a while loop to check the collision
    while n > 1:
        collision = False
        for i in range(n-1):
            if i == 0 or i == n-1:
                continue
            if n % i == 0:
                collision = True
                break
        if not collision:
            n -= 1
        else:
            print(n)
            
    # 2nd approach: use a loop to check the collision
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if n % i == 0:
                collision = True
                break
        if not collision:
            print(n)
            
    # 3rd approach: use a loop to check the collision
    for i in range(n):
        collision = False
        for j in range(n-1):
            if j == i:
                continue
            if n % j == 0:
                collision = True
                break
        if not collision:
            print(n)
            
    # 4th approach: use a recursive and a while loop
    while n > 1:
        collision = False
        for i in range(n-1):
            if i == 0 or i == n-1:
                continue
            if n % i == 0:
                collision = True
                break
        if not collision:
            n -= 1
        else:
            print(n)
            
    # 5th approach: use a loop to check the collision
    for i in range(n):
        collision = False
        for j in range(n):
            if i == j:
                continue
            if n % i == 0:
                collision = True
                break
        if not collision:
            print(n)
            
    # 6th approach: use a while loop and use the modulo operator
    while n > 1:
        collision = False
        for i in range(n-1):
            if i == 0 or i == n-1:
                continue
            if n % i == 0:
                collision = True
