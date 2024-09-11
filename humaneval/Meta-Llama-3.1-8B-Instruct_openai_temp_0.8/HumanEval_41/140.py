**Car Collision Calculator**
==========================

The following Python script calculates the number of collisions between two sets of cars driving in opposite directions.

```python
def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions between two sets of cars driving in opposite directions.

    Args:
    n (int): The number of cars driving in each direction.

    Returns:
    int: The total number of collisions.
    """
    def gcd(a, b):
        """Compute the greatest common divisor of a and b"""
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        """Compute the lowest common multiple of a and b"""
        return a * b // gcd(a, b)

    return lcm(n, n)


# Example usage
if __name__ == "__main__":
    n = 10
    collisions = car_race_collision(n)
    print(f"The number of collisions for {n} cars in each direction is: {collisions}")
```

**Explanation**
---------------

This script uses the mathematical principles of greatest common divisors (GCD) and lowest common multiples (LCM) to calculate the number of collisions. The GCD of two numbers is the largest number that divides both numbers without leaving a remainder. The LCM of two numbers is the smallest number that is a multiple of both numbers.

The `car_race_collision` function takes the number of cars driving in each direction as input and returns the total number of collisions. It uses the `gcd` function to compute the GCD of the number of cars in each direction and the `lcm` function to compute the LCM. The LCM is equal to the number of collisions.

The example usage at the end of the script demonstrates how to call the `car_race_collision` function with a given number of cars and print the result.