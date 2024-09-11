```python
def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left. The two sets of cars start out being very far from
    each other. All cars move in the same speed. Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # The problem can be solved by calculating the number of possible pairs
    # of left-moving and right-moving cars. Since the order of cars in each
    # direction doesn't matter, we can calculate this using combinations.
    from math import comb

    # Calculate the number of combinations of n cars taken 2 at a time
    # (each representing a pair of left-moving and right-moving cars)
    num_collisions = comb(n, 2)

    return num_collisions

# Test the function
print(car_race_collision(5))  # Example usage
```

This script uses the combination formula to calculate the number of possible pairs of left-moving and right-moving cars, which corresponds to the number of collisions. The combination formula is calculated as `n! / (r! * (n-r)!)`, where `n` is the total number of cars and `r` is the number of cars taken at a time. In this case, `r` is 2. The `math.comb` function in Python calculates this for us, making the code more concise.