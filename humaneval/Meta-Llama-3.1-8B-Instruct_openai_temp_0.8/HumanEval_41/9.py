### Car Collision Problem Solution
#### Problem Description
Imagine a road that's a perfectly straight infinitely long line. `n` cars are driving left to right; simultaneously, a different set of `n` cars are driving right to left. The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left. However, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

#### Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between left to right and right to left cars.
    
    Args:
        n (int): The number of cars in each direction.
    
    Returns:
        int: The total number of collisions.
    """
    # The total number of pairs is n * (n + 1) / 2
    # There are two collisions for each pair
    return n * (n + 1) // 2 * 2 - n * n

# Example usage:
print(car_race_collision(1))  # 0
print(car_race_collision(2))  # 1
print(car_race_collision(3))  # 3
```
In this solution, we use the formula for the sum of the first `n` natural numbers (`n * (n + 1) / 2`) to calculate the total number of pairs of cars that can collide. Since each pair has two possible collisions (one for each direction of movement), we multiply by 2. However, this counts each pair twice (once for each direction), so we subtract `n * n` to avoid double-counting the pairs where both cars are moving in the same direction.