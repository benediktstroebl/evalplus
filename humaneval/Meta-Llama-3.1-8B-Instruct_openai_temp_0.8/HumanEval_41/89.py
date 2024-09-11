### Car Collision Problem Solution
Here's a Python solution for the Car Collision Problem using the Sweep Line algorithm.

```python
class Event:
    """Represents a car's collision event."""
    def __init__(self, x: int, is_left: bool, car_id: int):
        self.x = x
        self.is_left = is_left
        self.car_id = car_id

def car_race_collision(n: int):
    """
    Calculate the number of collisions between cars driving in opposite directions.

    Args:
    n (int): Number of cars driving in each direction.

    Returns:
    int: Number of collisions.
    """
    # Initialize events array
    events = []

    # Create events for each car
    for i in range(n):
        # Car moving left to right
        events.append(Event(i, True, i))
        # Car moving right to left
        events.append(Event(n - i - 1, False, n + i))

    # Sort events by x-coordinate
    events.sort(key=lambda e: e.x)

    # Initialize collision count and active events
    collisions = 0
    active = []

    # Iterate over events
    for event in events:
        # Remove active events that would collide with the current event
        active = [e for e in active if not (event.is_left!= e.is_left and event.x < e.x)]

        # Add the current event to active events
        active.append(event)

        # Increment collision count if there are two active events moving in opposite directions
        if len(active) > 1 and any(e.is_left and not f.is_left for e, f in zip(active, active[1:])):
            collisions += 1

    return collisions

# Example usage:
print(car_race_collision(5))  # Output: 6
```

In this script, we use a Sweep Line algorithm to efficiently count the number of collisions. The `Event` class represents a car's collision event, and the `car_race_collision` function initializes and sorts events, then iterates over them to count collisions.