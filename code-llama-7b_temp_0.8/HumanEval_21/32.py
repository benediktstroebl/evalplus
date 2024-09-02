from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # accumulate the numbers
    total = sum(numbers)

    # calculate the largest absolute number
    largest = max(abs(number) for number in numbers)

    # for each number, calculate the percent of the total
    percent = []
    for number in numbers:
        if largest != 0:
            percent.append(100 * abs(number) / largest)
        else:
            percent.append(0)

    # rescale the numbers to be a percent
    percent_rescaled = [percentage / 100 for percentage in percent]

    # for each number, calculate the difference between the smallest and largest
    range_of_numbers = max(percent_rescaled) - min(percent_rescaled)

    # rescale the numbers to be between 0 and 1
    rescaled = [(percent - min(percent_rescaled)) / range_of_numbers for percent in percent_rescaled]

    return rescaled

