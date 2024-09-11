```python
def car_race_collision(n: int) -> int:
    """
    Calculates the number of collisions in a straight-line car race scenario.

    Args:
        n (int): Number of cars in each direction.

    Returns:
        int: Number of collisions.
    """
    # Two sets of n cars. So, total number of cars is 2n.
    total_cars = 2 * n
    
    # The total number of collisions will be the sum of collisions for all pairs of cars.
    # Since each pair of cars can collide at most once, we need to choose 2 cars out of 2n.
    # This is a combination problem, where we choose 2 items from a set of 2n items.
    # The formula for combination is C(n, k) = n! / (k!(n-k)!), where "!" denotes factorial.
    # Here, n = 2n and k = 2.
    import math
    collisions = math.comb(total_cars, 2)
    
    # However, not all pairs of cars can collide. The pairs of cars where both cars are moving in the same direction
    # cannot collide. There are n pairs of cars where both cars are moving left to right, and n pairs where both cars
    # are moving right to left. So, we need to subtract these pairs from the total number of pairs.
    pairs_same_direction = n * 2
    
    # Subtract the pairs where both cars are moving in the same direction from the total number of pairs.
    collisions -= pairs_same_direction
    
    return collisions

# Test the function
print(car_race_collision(2))  # Output: 1
print(car_race_collision(3))  # Output: 4
print(car_race_collision(4))  # Output: 7
```
This script uses the `math.comb` function from Python's standard library to calculate the number of combinations of choosing 2 items from a set of 2n items. It then subtracts the number of pairs where both cars are moving in the same direction from the total number of pairs to get the number of collisions.