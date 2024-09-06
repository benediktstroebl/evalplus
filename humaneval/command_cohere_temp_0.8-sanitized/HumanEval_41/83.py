def car_race_collision(n: int):
    rolling_left = 0
    rolling_right = 0
    collisions = 0

    for i in range(n):
        rolling_left += i
        rolling_right += (n - i - 1)

        # Count collisions between cars rolling in opposite directions:
        collisions += min(rolling_left, rolling_right)

        # Reset counts for the next iteration:
        rolling_left %= (2 * n)
        rolling_right %= (2 * n)

    return collisions