
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
    if not arr or k > len(arr): return []

    # my solution
    def merge_sorted_arrays(arr1, arr2):
        """
        Merge two sorted arrays into one.
        """
        i = j = 0
        res = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        # append the remaining items in arr1 or arr2
        res.extend(arr1[i:] or arr2[j:])

        return res

    arr.sort()

    return arr[-k:] if k == 1 else merge_sorted_arrays(arr[-k+1:], [arr[-k]])

    # others' solution
    # use max heap to solve this problem
    import heapq
    heap = [-1] * k
    for n in arr:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return [-x for x in heap]

    # another solution
    # use merge sort to solve this problem
    def merge_sort(arr, k):
        """
        Merge sort the given list in place.
        """
        def helper(arr, left, right):
            if left >= right: return

            mid = (left + right) // 2
            helper(arr, left, mid)
            helper(arr, mid + 1, right)
            merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            """
            Merge two sorted lists (subarrays) into one.
            """
            i, j = left, mid + 1
            k = left
            while i <= mid and j <= right:
                if arr[i] < arr[j]:
                    res[k] = arr[i]
                    i += 1
                else:
                    res[k] = arr[j]
                    j += 1
               
