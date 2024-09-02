
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # Use heapq.heappush to keep adding elements to heap
    heap = []
    for num in nums:
        heapq.heappush(heap, (num, sum(map(int, str(num)))) if str(num) != '0' else (num, sum(map(int, str(num)))) + (0,))

    heapq.heappop(heap)
    return sorted(heap, key=lambda x: x[1], reverse=True)
