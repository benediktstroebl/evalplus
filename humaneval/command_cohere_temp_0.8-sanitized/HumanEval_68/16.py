import collections
def pluck(arr):
    # Create a min-heap of tuples with (value, index) using the heapq module
    heap = collections.heapq
    min_heap = [(val, i) for i, val in enumerate(arr)]
    heapq.heapify(min_heap)

    # Pull the smallest even value (if exists), otherwise pull the smallest value
    while min_heap and not isinstance(min_heap[0][0], int) or min_heap[0][0] % 2:
        heapq.heappop(min_heap)
    ans = []
    if min_heap:
        ans = [min_heap[0][0], min_heap[0][1]]
    return ans if ans else []