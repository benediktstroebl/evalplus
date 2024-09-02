

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

    print('Car Race Collision Problem')
    print('Given:')
    print('n =', n)
    print('We need to find the number of times two cars collide.')
    print('_____________________________________________')

    print('Approach:')
    print('Suppose that we can find the number of times a car hits a car moving in the opposite direction.')
    print('However, the number of hits between two cars is equal to zero.')
    print('Therefore, there must be at least one car that hits a car moving in the opposite direction.')
    print('This means that there must be a car moving in the opposite direction that is hit by another car moving in the opposite direction.')
    print('The number of times two cars collide is equal to the sum of the number of times the cars hit in the opposite direction.')
    print('_____________________________________________')

    print('The number of times two cars hit in the opposite direction is:')
    print(int(n*(n-1)//2))
    print('_____________________________________________')

    print('Discussion:')
    print('This can be done with a math formula
