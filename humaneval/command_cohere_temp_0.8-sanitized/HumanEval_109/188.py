import heapq
from collections import Counter
def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True

    # Count occurrences of each element
    counter = Counter(arr)
    
    # Create a min heap with (frequency, element) pairs
    heap = []
    for elem, freq in counter.items():
        heapq.heappush(heap, (-freq, elem))

    # Initialize result
    result = False

    # Remove elements from the heap until it becomes empty
    while heap:
        freq, elem = heapq.heappop(heap)

        # If there is a single element left, it can be placed at the 0th index
        if len(heap) == 1 and freq == 1:
            result = True
            break

        # If the frequency of the current element is 1, it can be placed at the end
        if freq == 1:
            result = True
            continue

        # Otherwise, we need at least two right shifts to place it in the correct position
        num_shifts = -(len(heap) - 1) // 2
        if num_shifts >= 0:
            result = True
            break

    return result