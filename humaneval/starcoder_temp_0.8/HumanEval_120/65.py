
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # # Sorting
    # arr.sort(reverse=True)
    # return arr[:k]

    # # Heap
    # heap = arr[:k]
    # heapq.heapify(heap)
    # for i in range(k, len(arr)):
    #     heapq.heappushpop(heap, arr[i])
    # return heap

    # # Buckets
    # buckets = [[] for _ in range(k+1)]
    # for num in arr:
    #     idx = k
    #     while idx > 0 and num > arr[idx-1]:
    #         idx -= 1
    #     buckets[idx].append(num)
    # return [max(bucket) for bucket in buckets]

    # # Quickselect
    # def partition(lo, hi):
    #     i = lo
    #     j = hi + 1
    #     v = arr[lo]
    #     while True:
    #         while True:
    #             i += 1
    #             if i == hi or arr[i] >= v:
    #                 break
    #         while True:
    #             j -= 1
    #             if j == lo or arr[j] <= v:
    #                 break
    #         if i >= j:
    #             break
    #         arr[i], arr[j] = arr[j], arr[i]
    #     arr[lo], arr[j] = arr[j], arr[lo]
    #     return j
    # def select(lo, hi, k_smallest):
    #     i = lo
    #     j = hi
    #     while i < j:
    #         pivot = partition(i, j)
    #         if pivot == k_smallest:
    #             return
    #         elif pivot < k_smallest:
    #             i = pivot + 1
    #         else:
    #             j = pivot - 1
    # select(0, len(arr)-1, k)
    # return arr[:k]

    # # Quickselect with random pivot
    # def randomized_partition(lo, hi):
    #     i = random.randint(lo, hi)
    #     arr[lo], arr[i] = arr[i], arr[lo]
    #     return partition(lo, hi)
    # def randomized_select(lo,
