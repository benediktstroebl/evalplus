def pluck(arr):
    if not arr:
        return []

    # Use a min heap to efficiently find the smallest even value and its index.
    min_heap = []
    min_heap_idx = []
    for i, num in enumerate(arr):
        if num % 2 == 0:
            heappush(min_heap, (-num, i))
            min_heap_idx.append(i)

    if min_heap:
        # Pop the smallest even value and its index from the heap.
        smallest_even_val, smallest_even_idx = heappop(min_heap)
        return [smallest_even_val, smallest_even_idx]

    # If no even values are found, return the smallest value (index not considered).
    return [min(arr), min_heap_idx[0] if min_heap_idx else 0]
def heappop(heap):
    if not heap:
        return None
    smallest = heap[0]
    heap.pop(0)
    heapify(heap)
    return smallest