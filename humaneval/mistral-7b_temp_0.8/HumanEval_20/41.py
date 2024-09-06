

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # The distance between two numbers is their absolute difference
    def distance_between_two(x: float, y: float) -> float:
        return abs(x - y)

    # Two values in the list are the closest when their distance is the smallest.
    # Therefore, we need to find the smallest distance between two numbers in the list.
    # To do so, we iterate through all the possible combinations and find the smallest one.
    # To simplify our code, we can use a helper function `is_closer_than`

    def is_closer_than(distance1: float, distance2: float) -> bool:
        return distance1 < distance2

    def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
        # We have to ensure that the input list has at least two values
        assert len(numbers) >= 2, "The input list must contain at least two values."

        # We find the smallest distance between two numbers in the list
        min_distance = min(distance_between_two(x, y) for x in numbers
