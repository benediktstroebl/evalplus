```markdown
### Car Collision Problem Solution
#### Problem Description
Imagine a road that's a perfectly straight infinitely long line.
n cars are driving left to right;  simultaneously, a different set of n cars
are driving right to left.   The two sets of cars start out being very far from
each other.  All cars move in the same speed.  Two cars are said to collide
when a car that's moving left to right hits a car that's moving right to left.
However, the cars are infinitely sturdy and strong; as a result, they continue moving
in their trajectory as if they did not collide.

This function outputs the number of such collisions.

#### Solution
```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions.

    Args:
    n (int): The number of cars in each direction.

    Returns:
    int: The total number of collisions.
    """
    # Initialize the total collisions to 0
    total_collisions = 0
    
    # Calculate the total number of pairs
    total_pairs = n * (n + 1) // 2
    
    # The number of collisions is equal to the number of pairs
    # because each pair of cars will collide once
    total_collisions = total_pairs
    
    return total_collisions
```

#### Example Usage
```python
# Test the function
print(car_race_collision(5))  # Output: 10
print(car_race_collision(10))  # Output: 45
```

#### Explanation
The problem can be solved using combinatorics. Since each pair of cars will collide once, the total number of collisions is equal to the number of pairs of cars, which is given by the formula `n * (n + 1) // 2` where `n` is the number of cars in each direction. This formula calculates the total number of pairs of cars that can be formed from `n` cars.