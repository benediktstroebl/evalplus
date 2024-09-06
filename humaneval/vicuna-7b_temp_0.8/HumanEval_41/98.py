

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
    # In this case, we can use dynamic programming by considering all possible combinations of the positions of cars
    # and then checking whether there are any collisions or not.
    # This way, we can avoid the O(n^2) time complexity.
    # We'll do a depth-first search (DFS) to check for collisions.

    # Initialize a variable to count the number of collisions
    collision_count = 0
    
    # We'll use a queue to perform the DFS
    queue = [(0, n-1)] # start with the leftmost car at position 0 and the rightmost car at position n-1
    
    # While the queue is not empty, we pop the first pair of positions and perform a DFS
    while queue:
        # Pop the first pair of positions
        current_pos_left, current_pos_right = queue.pop(0)
        
        # Check for collisions
        for i in range(current_pos_left, current_pos_right):
            collision_count += 1
        
        # Add the positions to the queue
        queue.append((current_pos_left, current_pos_right))
    
    # Return the number of collisions
    return collision_count