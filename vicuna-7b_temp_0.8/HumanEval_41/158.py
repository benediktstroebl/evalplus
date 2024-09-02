

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
    # your code here
    # To solve this problem, we can use a combination of two techniques:
    # 1. calculating the number of ways to pick the two cars that collide
    # 2. calculating the number of ways to pick the two cars that do not collide
    # 
    # Let's start by counting the number of ways to pick the two cars that collide.
    # We can use the principle of combination to solve this problem.
    # Let's assume that the two cars that collide are car i and j.
    # The number of ways to pick car i is C(n,2), since there are two cars to choose from.
    # The number of ways to pick car j is also C(n,2), since there are two cars to choose from.
    # The total number of ways to pick the two cars that collide is C(n,2) x C(n,2),
    # since there are two cars to choose from for each of the two cars that collide.
    # Let's call this number S.
    # 
    # Now, let's count the number of ways to pick the two cars that do not collide.
    # We can do this by using the principle of combination as well.
    # Let's assume that the two cars that do not collide are car i and j.
    # The number of ways to pick car i is C(n,2), since there are two cars to choose from.
    # The number of ways to pick car j is also C(n,2), since there are two cars to choose from.
    # The total number of ways to pick the two cars that do not collide is C(n,2) x C(n,2),
    # since there are two cars to choose from for each of the two cars that do not collide.
    # Let's call this number T.
    # 
    # S + T = total number of combinations of two elements from n-2 cars
    # 
    # Now, we need to find S and T.
    # 
    # To calculate S, we need to multiply the number of ways to pick the two cars that collide
    # by the number of ways to pick the two cars that do not collide
