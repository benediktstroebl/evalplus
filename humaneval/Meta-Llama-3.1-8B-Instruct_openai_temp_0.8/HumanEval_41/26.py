```python
def car_race_collision(n: int):
    """
    This function calculates the number of collisions that occur between two sets of n cars,
    where one set of cars moves left to right and the other set moves right to left,
    at the same speed and infinitely sturdy.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The number of collisions that occur.
    """
    # Sort all car positions from 0 to 2n
    # These are the potential collision points
    collisions = n * (n - 1) // 2
    return collisions

print(car_race_collision(5))  # Example usage
```

This script uses a mathematical approach to solve the problem, based on the concept of combinations (choosing 2 cars out of n to collide). 

Explanation:
- Since all cars move at the same speed, the order in which cars from each set appear does not matter.
- Therefore, any pair of cars from the two sets can potentially collide.
- The total number of cars is 2n, and we need to choose 2 cars out of 2n to collide. However, in this scenario, we're choosing a car from the car traveling left to right and the car traveling right to left. 
- Hence, the number of potential collision points is the same as the number of ways to choose 2 cars out of n, which is n*(n-1)/2.
- Therefore, the number of potential collisions is n*(n-1)/2. This is the formula used in the code.