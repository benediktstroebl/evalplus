```python
def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars driving left to right; simultaneously, a different set of n cars are driving right to left.
    The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars will meant to collide when a car that's moving left to right hits a car that's moving right to left.
    If cars are infinitely sturdy and strong, as a result, they continue moving in their trajectory as if they did not collide.
    return: 
    A list of tuples containing the number of left-moving and right-moving cars that hit each other.
    """
 cars are sorted by their speed in ascending order.
    """
    left_right_speed = []
    for i in range(n):
        left_right_speed.append((left driving right to left, 0, i, n-i)
    for j in range(n):
        if i == j: continue
        elif left_right_speed[i][1] < left_right_speed[j][1]:
            left_right_speed[j][0] = 1
        else:
            left_right_speed[j][0] = 1
    return left_right_speed
```