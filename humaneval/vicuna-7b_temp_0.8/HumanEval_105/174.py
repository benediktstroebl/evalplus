
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    if not arr:
        return []
    n = len(arr)
    # use a heap to sort the array
    heap = [arr[0]]
    while len(heap) > 1:
        i = 0
        l = heap[0]
        h = heap[0]
        while i <= n and l < n and l - i >= 2:
            if l - i - 1 in arr and arr[l - i - 1] < arr[l]:
                heap[0] = arr[l - i - 1]
                heap[1] = l
                l += 1
            else:
                heap[0] = l
                heap[1] = l
                l += 1
            i += 1
        if i <= n and l < n and l - i >= 2:
            heap[0] = arr[l]
            heap[1] = l
            l += 1
        else:
            heap[0] = arr[i]
            heap[1] = arr[i]
            i += 1
    return heap[2:]