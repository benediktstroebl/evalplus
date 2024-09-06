
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
    
    '''
    Here are the steps:
    1. if arr[i] < 10 then add arr[i] to the current sum
    2. else get the sum of the current sum and the current element (arr[i]) and add it to the current sum
    '''
    
    current_sum = 0
    for num in arr:
        if num < 10:
            current_sum += num
        else:
            current_sum += sum([num])
        if current_sum >= k:
            return current_sum
            
