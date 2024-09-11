```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of car collisions in a simultaneous race.
    
    Parameters:
    n (int): Number of cars in each direction.
    
    Returns:
    int: Number of car collisions.
    """
    # Initialize collision counter to 0
    collisions = 0
    
    # Iterate over the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Each collision corresponds to a pair of two cars
        # Therefore, the total number of collisions is given by the sum of all numbers
        # from 1 to n, which is equal to n * (n + 1) / 2
        collisions += i
    
    return collisions

# Example usage
if __name__ == "__main__":
    n = 5  # number of cars in each direction
    result = car_race_collision(n)
    print(f"Number of collisions with {n} cars in each direction: {result}")
```

This script defines a function `car_race_collision` that takes the number of cars `n` as an input and returns the number of collisions. The function uses a simple mathematical formula to calculate the number of collisions, which is given by the sum of all numbers from 1 to `n`, or `n * (n + 1) / 2`. This formula is derived from the fact that each collision corresponds to a pair of two cars. The script then demonstrates the function's usage with an example.