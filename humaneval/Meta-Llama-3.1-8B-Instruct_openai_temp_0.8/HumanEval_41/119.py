```python
def car_race_collision(n: int):
    """
    Calculates the number of collisions between two sets of n cars driving in opposite directions.

    Args:
        n (int): The number of cars in each set.

    Returns:
        int: The total number of collisions.
    """
    # The two sets of cars can be represented as two sequences of 1s and 0s.
    # A 1 represents a car driving left to right, and a 0 represents a car driving right to left.
    # If a 1 and a 0 are adjacent, it means there's a collision.
    # Therefore, we need to find the number of inversions between the two sequences.
    # We can use the concept of inclusion-exclusion from combinatorics.

    # Initialize a counter for the total number of inversions.
    total_inv = 0

    # The first set of cars is represented by a sequence of 1s.
    # We want to find the number of inversions with this sequence.
    # This is equivalent to finding the number of inversions in the sequence of 1s itself,
    # which is the number of pairs of elements that are out of order.
    # The number of inversions in a sequence of length n is given by the formula: n*(n-1)/2.
    total_inv += n * (n - 1) // 2

    # Now, we want to find the number of inversions with the second set of cars.
    # However, this is equivalent to finding the number of inversions in the first sequence
    # with the elements in the second sequence.
    # Therefore, we need to add this value to the total number of inversions.
    total_inv += n * (n - 1) // 2

    # However, we counted each inversion twice, so we need to subtract the number of inversions
    # in the sequence of 1s with the elements in the second sequence.
    # This is equivalent to finding the number of inversions in the first sequence itself,
    # which is the number of pairs of elements that are out of order.
    # The number of inversions in a sequence of length n is given by the formula: n*(n-1)/2.
    total_inv -= n * (n - 1) // 2

    # Finally, we need to return the total number of inversions modulo 2, because each collision
    # corresponds to an inversion, and we want the total number of collisions.
    return total_inv % 2

# Test the function
print(car_race_collision(2))  # Expected output: 1
print(car_race_collision(3))  # Expected output: 1
print(car_race_collision(5))  # Expected output: 1
```

This script calculates the total number of collisions between two sets of n cars driving in opposite directions. The approach is based on the concept of inclusion-exclusion from combinatorics. The total number of collisions is equivalent to the total number of inversions between the two sequences, which is the sum of the number of inversions in each sequence, minus the number of inversions in the intersection of the two sequences. The result is returned modulo 2, because each collision corresponds to an inversion.