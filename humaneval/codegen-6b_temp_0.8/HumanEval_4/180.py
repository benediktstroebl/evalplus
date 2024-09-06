from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check inputs
    if not isinstance(numbers, list):
        raise TypeError("Input variable is not of type list.")
    # Check if all inputs are of type float
    if not all(isinstance(n, float) for n in numbers):
        raise TypeError("All elements of input list should of type <float>.")
    # Check if there are more than one element.
    if len(numbers) < 2:
        raise ValueError("There is less than two elements in the list.")

    # Calculate the mean and arrange the input list
    mean = sum(numbers)/len(numbers)
    numbers.sort()
    # For any element, absolute difference from mean is equal to the distance
    # from previous element and from the next element.
    differences = [abs(n - mean) for n in numbers]
    # Average is the sum divided by the count
    deviation = sum(differences)/len(differences)
    return deviation

