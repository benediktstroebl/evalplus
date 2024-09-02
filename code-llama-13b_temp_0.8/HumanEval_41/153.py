

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
    # The intuition here is to realize that if we have two cars, the number of
    # collisions depends on how many cars are to the left and how many cars are to the right.
    # We can easily use the binomial coefficient to solve this problem, for example
    # for n=3 we get 3 cars on the left, and 3 cars on the right, and the number of collisions
    # is 6.  This is just nC2 (combination) because each car on the left is going to collide
    # with each car on the right.
    # Now, to solve the case with n cars, we can make a recurrence, where we simply
    # sum over all the possible number of cars to the left and right.
    # E.g. if we have n=3 cars, then we can have 1 to the left and 2 to the right,
    # 2 to the left and 1 to the right, and 0 to the left and 3 to the right.
    # Now, to do this we can use the binomial coefficient again, and we get:
    # num_collsions = nC1 + 2nC2 + 3nC3 ... (n-1)nC(n-1) + nCn
    # = n(n+1)C(n+1)/2
    # = n(n+1)/2 choose n.
    # This is because the nCi binomial coefficients sum to n(n+1)/2 choose n,
    # and we can use the pascal's triangle property to get the result.
    #
    # Now we can solve the problem using the closed form formula for the binomial coefficient
    # which is nCk = n! / (k! * (n-k)!)
    # This is the same formula we used to find factorial in the factorial_recursive function.
    # So, we get that nCk = n!/(k! * (n-k)!) = n*n*(n-1)...(n-k+1)/k!/(n-k)!
    # = n(n-1)(n-2)...(n-k+1)/k!
    # So we can see
