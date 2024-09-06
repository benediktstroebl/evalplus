from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Using generators to iterate over lists of numbers
    # generator = (x for x in numbers)
    # generators closer to each other than threshold
    close_pairs = ((x, y) for x, y in zip(generators) if abs(x - y) < threshold)
    return bool(close_pairs)