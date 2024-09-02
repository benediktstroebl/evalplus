
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
    def maxHeapify(arr, i, n):
        #assume 0 indexed
        #assume root is a heap
        #but i might not be
        #find out if i is a heap or not
        largest = i
        left = 2*i + 1 #left child of root
        right = 2*i + 2 #right child of root

        #if left child exists and is greater than root
        if left < n and arr[left] > arr[largest]:
            largest = left
        #if right child exists and is greater than root
        if right < n and arr[right] > arr[largest]:
            largest = right

        #if root is not a heap
        if largest != i:
            #swap root and largest
            arr[largest], arr[i] = arr[i], arr[largest]
            #heapify largest
            maxHeapify(arr, largest, n)

    def buildMaxHeap(arr, n):
        #iterate from n/2 to 0
        for i in range(n//2 - 1, -1, -1):
            #heapify all internal nodes in the tree
            maxHeapify(arr, i, n)

    #build max heap
    n = len(arr)
    buildMaxHeap(arr, n)
    #iterate k times
    for i in range(k):
        #swap root and last element
        arr[0], arr[n - 1] = arr[n - 1], arr[0]
        #heapify root
        maxHeapify(arr, 0, n - 1)
        #decrement n
        n -= 1

    return arr[:k]

