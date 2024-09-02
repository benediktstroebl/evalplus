

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

    # distance[i] stores the distance between the cars moving in opposite directions,
    # assuming the cars are moving in the same speed.
    distance = [0] * n

    # current[i] stores the index of the car moving in the opposite direction,
    # i.e., the current collision point.
    current = [0] * n

    # s[i] is a stack storing the indices of the cars moving in the same direction.
    # The current collision point is the top element of the stack.
    s = Stack()

    for i in range(n):
        # If the stack is empty, the new car is moving in the same direction.
        if s.empty():
            s.push(i)

        # If the stack is not empty, compare the distance between the new car and the
        # current collision point to the distance between the current collision point
        # and the previous collision point.
        else:
            d = (2 * i - current[s.peek()]) % n
            if distance[d] > i - s.peek():
                # If the distance is smaller, the new car is moving in the same
                # direction.
                distance[d] = i - s.peek()
                current[s.peek()] = i
            else:
                # If the distance is larger or equal, the new car is moving in the
                # opposite direction.
                s.pop()

        # Now the stack stores the index of the cars moving in the same direction.
        # Therefore, the current collision point is the top element of the stack.
        if not s.empty():
            current[i] = s.peek()

    return current[n - 1]
