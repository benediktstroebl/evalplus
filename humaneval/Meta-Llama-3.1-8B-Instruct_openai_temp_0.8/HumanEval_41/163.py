```python
def car_race_collision(n: int):
    """
    Returns the number of collisions between two sets of n cars driving in opposite directions.
    
    :param n: The number of cars in each set.
    :return: The number of collisions between the two sets of cars.
    """
    return (n * (n - 1)) // 2

# Test the function
print(car_race_collision(5))  # Output: 10
```

In this script, we calculate the number of collisions using the formula for the sum of an arithmetic series. The two sets of `n` cars each have `n` collisions, but we divide by 2 because each collision is counted twice (once for each set). However, we also subtract 1 from `n` to avoid counting each pair of cars twice. The formula `(n * (n - 1)) // 2` calculates the sum of the first `n-1` positive integers, which is equivalent to the number of pairs of cars that collide.