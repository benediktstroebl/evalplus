
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # find kth smallest element, and then sum elements smaller than that element
    from collections import defaultdict
    from bisect import bisect_left
    import heapq
    heap = []
    d = defaultdict(int)
    for x in arr[:k]:
        heapq.heappush(heap, x)
        d[x] += 1
    max_element = heapq.nsmallest(1, heap)[0]

    result = 0
    for x in arr:
        if x <= max_element:
            result += x
        else:
            heapq.heappush(heap, x)
            if x < max_element:
                max_element = x
            else:
                continue
            while len(heap) > k:
                if heap[0] == max_element:
                    heapq.heappop(heap)
                    max_element = heapq.nsmallest(1, heap)[0]
                else:
                    break
    return result

