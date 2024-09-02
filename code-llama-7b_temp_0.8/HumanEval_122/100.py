
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
    import heapq

    max_heap = list(map(abs, arr[:k]))
    heapq.heapify(max_heap)

    total = 0
    for i in range(k, len(arr)):
        if len(max_heap) == 1:
            if abs(arr[i]) <= max_heap[0]:
                total += arr[i]
                heapq.heappushpop(max_heap, arr[i])
            else:
                break
        elif len(max_heap) == 2:
            if abs(arr[i]) <= max_heap[0] and arr[i] >= max_heap[1]:
                total += arr[i]
                heapq.heapreplace(max_heap, arr[i])
            elif abs(arr[i]) <= max_heap[1]:
                total += arr[i]
                heapq.heappushpop(max_heap, arr[i])
            else:
                break
        else:
            break

    return total


