from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    return [x for x in numbers if x not in seen and seen.add(x)]


def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    """ Merge two overlapping intervals, taking the union of their interiors.
    Return a list of Interval objects with the merged intervals.
    """
    intervals_with_duplicates = remove_duplicates(intervals)
    return [merge(interval) for interval in intervals_with_duplicates]

def merge(interval1: Interval, interval2: Interval) -> Interval:
    """ Merge two intervals using their start and end times and the maximum of their length.
    """
    max_length = max(interval1.start_time, interval2.start_time)
    return Interval(max_length, interval1.end_time or interval2.end_time)

def process_intervals(intervals: List[Interval]) -> None:
    """Process the intervals and merge them into larger intervals.
    Keep track of the total length of intervals as we process them.
    """
    total_length = 0
    for interval in intervals:
        total_length += interval.length
    intervals = merge_intervals(intervals)
    print(f"Total length of intervals processed: {total_length} seconds")

if __name__ == '__main__':
    intervals = [
        Interval(1, 2),
        Interval(3, 4),
        Interval(2, 4),
        Interval(4, 5),
    ]
    process_intervals(intervals)