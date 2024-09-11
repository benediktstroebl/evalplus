```python
def car_race_collision(n: int):
    """
    Calculates the number of car collisions in a simultaneous car race.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The total number of collisions.
    """
    def catalan(n):
        """
        Calculates the nth Catalan number using dynamic programming.
        Catalan numbers represent the number of ways to balance n pairs of brackets.
        """
        if n == 0 or n == 1:
            return 1
        catalans = [0]*(n+1)
        catalans[0] = catalans[1] = 1
        for i in range(2, n+1):
            catalans[i] = 0
            for j in range(i):
                catalans[i] += catalans[j] * catalans[i-j-1]
        return catalans[n]

    # The number of collisions is equal to the (2n)th Catalan number
    return catalan(2*n)

# Example usage:
n = 3
print(f"Number of collisions with {n} cars in each direction: {car_race_collision(n)}")
```

This script defines a function `car_race_collision` that takes the number of cars in each direction as input and calculates the number of collisions. The function uses a helper function `catalan` to calculate the nth Catalan number using dynamic programming.

In a simultaneous car race with n cars in each direction, the number of collisions is equal to the (2n)th Catalan number. This is because each collision corresponds to a way to balance 2n pairs of brackets, and the Catalan number represents the number of such ways.

The example usage demonstrates how to use the `car_race_collision` function with 3 cars in each direction.