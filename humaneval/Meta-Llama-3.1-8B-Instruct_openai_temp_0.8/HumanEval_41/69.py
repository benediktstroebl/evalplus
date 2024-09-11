### Collision Detection in a Car Race
#### Problem Statement

Imagine a road that's a perfectly straight infinitely long line. `n` cars are driving left to right; simultaneously, a different set of `n` cars are driving right to left. The two sets of cars start out being very far from each other. All cars move in the same speed. Two cars are said to collide when a car that's moving left to right hits a car that's moving right to left. However, the cars are infinitely sturdy and strong; as a result, they continue moving in their trajectory as if they did not collide.

#### Solution
```python
def car_race_collision(n: int) -> int:
    """
    This function calculates the number of collisions in a car race scenario.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions.
    """
    # Initialize the total number of collisions to 0
    total_collisions = 0
    
    # Use the formula for triangular numbers to calculate the total number of collisions
    # This formula is derived from the fact that each new car can collide with all previous cars
    total_collisions = n * (n - 1) // 2
    
    return total_collisions
```

#### Example Use Cases
```python
# Test the function with 5 cars in each set
print(car_race_collision(5))  # Output: 10

# Test the function with 10 cars in each set
print(car_race_collision(10))  # Output: 45
```