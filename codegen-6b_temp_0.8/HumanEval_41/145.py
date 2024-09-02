

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
    assert(n > 1)

    # Resolution
    res_pos = 1
    res_neg = 1
    while abs(res_pos - res_neg) > 1:
        # Set the resolution
        res_pos = res_neg
        res_neg = 0
        for i in range(len(pos)-1):
            for j in range(len(neg)-1):
                if abs(pos[i]-neg[j]) == (res_pos * 2):
                    res_pos = res_pos + 1
                    neg[j] = neg[j] + 1
                    pos[i] = pos[i] + 1
                    res_pos = res_pos + 1
                    break
                elif abs(pos[i]-neg[j]) == (res_pos * 2) + 1:
                    res_neg = res_neg + 1
                    pos[i] = pos[i] + 1
                    neg[j] = neg[j] + 1
                    res_neg = res_neg + 1
                elif abs(pos[i]-neg[j]) == (res_pos * 2) -1:
                    res_neg = res_neg + 1
                    pos[i] = pos[i] + 1
                    neg[j] = neg[j] + 1
                    res_neg = res_neg + 1
                elif abs(pos[i]-neg[j]) == (res_pos * 2) -2:
                    res_neg = res_neg + 1
                    pos[i] = pos[i] + 1
                    neg[j] = neg[j] + 1
                    res_neg = res_neg + 1
    return max(pos) + max(neg)

