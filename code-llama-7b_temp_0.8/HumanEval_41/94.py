

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
    # divide the road into two halves, left_half and right_half.
    # initially, the right_half contains n cars moving right to left,
    # and left_half is empty.
    # As time progress, the right_half is being driven at a constant speed
    # towards left_half, and car from left_half is being driven at a constant
    # speed towards right_half.
    # At time t, the size of right_half is rt_left + rt_right, where
    # rt_left = 2r + r(r - 1)/2, and rt_right = 2r.
    # So, if we set rt_left = rt_right = n, the size of right_half will be
    # n + n(n-1)/2 = n(n+1)/2.
    # And the size of left_half will be (n-1) + (n-1)(n-2)/2 = n(n-1)/2

    def car_race_collision_helper(n: int):
        if n == 0:
            return 0
        result = n
        i = 2
        while i <= n:
            result += i * (i - 1)
            i += 1
        return result
    return 2 * car_race_collision_helper(n)
