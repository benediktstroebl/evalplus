

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
    # sanity check
    assert(n > 0)

    # This is a classic dynamic programming problem.  Since we are looking for a recurrence relation
    # on the number of collisions, we can think of the cars as being in a line and the cars move
    # one at a time.  We can start at the beginning and move one car at a time in the forward direction
    # and count the collisions and move on to the next car in the next position in the forward
    # direction.  Then, we can think of the cars as being in a line and the cars move one at a time
    # in the reverse direction and count the collisions and move on to the next car in the next position
    # in the reverse direction.  Now we have 2 car sets moving in opposite directions.  So, we can add the
    # forward and reverse collisions and we have the total number of collisions.  By the time we get
    # to the end, we'll have counted all the collisions.

    # we'll use dynamic programming here.  We'll count the number of collisions we'll have at each position
    # in the line.  We'll start at the beginning and move forward and backward and sum up the number of collisions
    # at each position.

    # to make things easier, let's start with a two car problem

    # let's start with the first case where the first car is moving in the forward direction
    #  and the second car is moving in the backward direction.  That means the forward car
    #  is at position 0 and the backward car is at position n - 1.  This is the first collision
    #  since the cars are infinitely sturdy and strong and they continue to move forward in their
    #  trajectories.  We'll move on to the next position, the first car is at position 1 and
    #  the second car is at position n - 2.  Now we have a collision.  We'll move on to the next
    #  position, the first car is at position 2 and the second car is at position n - 3.  Now,
    #  we have no collision since the cars are infinitely sturdy and strong and they
