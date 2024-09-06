
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
    # # Method 1: Min-heap
    # import heapq
    # arr.sort()
    # result = []
    # for i in range(k):
    #     result.append(heapq.heappop(arr))
    # return result

    # Method 2: Quick Select
    # import random
    # pivot = random.choice(arr)
    # less, greater, equal = [], [], []
    # for x in arr:
    #     if x < pivot:
    #         less.append(x)
    #     elif x > pivot:
    #         greater.append(x)
    #     else:
    #         equal.append(x)
    # if len(equal) >= k:
    #     return equal[:k]
    # elif len(equal) + len(less) >= k:
    #     return less[:k-len(equal)] + equal
    # else:
    #     return less + equal + greater[:k-len(equal)-len(less)]

    # Method 3: Quick Sort
    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1

    def quick_sort(arr, left, right):
        if left < right:
            pivot_index = partition(arr, left, right)
            quick_sort(arr, left, pivot_index-1)
            quick_sort(arr, pivot_index+1, right)

    quick_sort(arr, 0, len(arr)-1)
    return arr[-k:]

