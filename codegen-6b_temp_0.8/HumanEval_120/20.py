
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
    
    def find_top_k(arr, k):
        if k == 0:
            return []
        if k == 1:
            return sorted(arr, reverse=True)

        max_heap = []
        for i in range(0, k):
            heappush(max_heap, -arr[i])

        for i in range(k, len(arr)):
            if -arr[i] > -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -arr[i])
        
        res = []
        for i in range(0, k):
            res.append(heappop(max_heap))

        return res

    def find_top_k_without_sort(arr, k):
        if k == 0:
            return []
        if k == 1:
            return arr

        result = []
        start = 0
        end = len(arr) - 1

        while start <= end:
            target_index = start
            current_min = arr[start]
            for i in range(start+1, end+1):
                if arr[i] > current_min:
                    target_index = i
                    current_min = arr[i]
            if len(result) < k:
                result.append(arr[target_index])
            else:
                if arr[target_index] > arr[result[0]]:
                    result[0] = target_index

            if len(result) < k:
                end = target_index-1
            else:
                start = target_index+1

        return result

    # return find_top_k(arr, k)
    return find_top_k_without_sort(arr, k)
