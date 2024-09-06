import unittest
def pluck(arr):
    if not arr:
        return []

    # Use a min heap to efficiently find the smallest even value node
    heap = []
    heapq.heappush(heap, [0, 0])  # Starting with a node with value 0 and index 0

    for i, value in enumerate(arr):
        # Even-valued nodes go into the min heap
        if value % 2 == 0:
            heapq.heappush(heap, [value, i])

        # If the current node is odd, we might have a smaller even value
        # node, so let's replace the current node in the heap if needed
        elif heapq.heappop(heap)[0] % 2 == 0:
            heapq.heappush(heap, [value, i])

    return [heapq.heappop(heap)[0], heapq.heappop(heap)[1]] if heap else []