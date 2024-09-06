

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
    # convert n to binary
    binary = "{0:b}".format(n)
    # add "0"s for size of binary
    binary += "0" * (9 - len(binary))
    # flip the string of 1s and 0s
    flipped_binary = [1 if b == "0" else 0 for b in binary]

    #max_collisions = 2 ** (len(flipped_binary) - 1)

    # figure out if there are any collisions
    #pos = 0
    #while pos < len(flipped_binary) - 1:
    #    if flipped_binary[pos] == 1:
    #        if flipped_binary[pos + 1] == 1:
    #            max_collisions -= 1
    #    pos += 1
    max_collisions = 2 ** (len(flipped_binary) - 1) - 1

    return max_collisions
