

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
    # You can use a 2D list to represent the cars, with the i-th element representing the i-th car's position
    # Initialize the number of collisions to 0
    n_collisions = 0
    
    # n cars in total, so n_cars/2 cars in each direction
    n_cars = n
    cars_left = [[] for _ in range(n_cars//2)]
    cars_right = [[] for _ in range(n_cars//2)]
    
    # Place the cars randomly in the 2D list
    for i in range(n_cars):
        cars_left[i].append(i)
        cars_right[i].append(n_cars - i - 1)
    
    # Let the cars move
    for i in range(n):
        # Find the index of the leftmost car in the left lane
        leftmost_index = [0 for _ in range(n_cars//2)]
        for j in range(n_cars):
            leftmost_index[j//2] = j if cars_left[j//2].pop(0) == i else j - 1
        
        # Find the index of the rightmost car in the right lane
        rightmost_index = [0 for _ in range(n_cars//2)]
        for j in range(n_cars):
            rightmost_index[j//2] = j if cars_right[j//2].pop(0) == i else j - 1
        
        # Update the positions of the cars
        for j in range(n_cars):
            if cars_left[j//2][leftmost_index[j//2]] != i:
                cars_left[j//2][leftmost_index[j//2]] = i
                n_collisions += 1
    
    return n_collisions
