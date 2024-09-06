

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
    results = []
    for i in range(n):
        results.append([0, 0])
    for i in range(2 * n):
        for j in range(n):
            # swap j and n-1-j if i%2 is 0
            if i % 2 == 0:
                if j == n - 1 - j:
                    results[j][i % 2] = results[j][1]
                else:
                    results[j][i % 2] += 1
            # swap j and -j if i%2 is 1
            else:
                if j == n - 1 - j:
                    results[j][1] = results[j][0]
                else:
                    results[j][1] += 1
    output = 0
    for res in results:
        output += res[0] * res[1]
    return output

