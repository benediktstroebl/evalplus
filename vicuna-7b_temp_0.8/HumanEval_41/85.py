

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
    # Your code here
    
    # Initialize variables
    cars_left = [None] * n
    cars_right = [None] * n
    for i in range(n):
        cars_left[i] = i + 1
        cars_right[i] = n + 1 - i

    # Find the first collision
    for i in range(n):
        for j in range(i, n):
            if cars_left[i] < cars_right[j] and cars_left[j] < cars_right[i]:
                print(f"Cars {cars_left[i]} and {cars_right[j]} collide")
                break

    # Find the last collision
    for i in range(n):
        for j in range(n - i):
            if cars_left[i] > cars_right[j] and cars_left[j] < cars_right[i]:
                print(f"Cars {cars_left[i]} and {cars_right[j]} collide")
                break

    # Find the middle collision
    for i in range(n // 2):
        for j in range(i + 1, n):
            if cars_left[i] < cars_right[j] and cars_left[j] < cars_right[i]:
                print(f"Cars {cars_left[i]} and {cars_right[j]} collide")
                break

    # Output the total number of collisions
    return n * (n + 1) // 2