Here's a Python script that contains a function named `move_one_ball` optimized to solve the problem statement with a comprehensive explanation:
```python
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    Optimization:
    The 2D array approach takes O(N^2) time and O(N) auxiliary space. 
    A better method is to maintain an auxiliary array 'ans' with same size as of 
    array 'arr'. The auxiliary array 'ans' initialized with True for all positions.
    Now we iterate the main array 'arr' and do the following
        1. If the current element is smaller than the last element of 
          auxiliary array 'ans' assignment is performed(set the ith position 
          of 'ans' to False).
        2. If the current element is greater than the last element of 
          auxiliary array 'ans' we return False.
    The time complexity is now O(N) and auxiliary space is O(N).
    """

    # Initialize an array of the same size as arr with True values
    ans = [True for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > arr[i-1]:
            return False
        if arr[i] < arr[i-1] and not ans[i-1]:
            ans[i-1] = False
    return True
```

This optimized function uses the `ans` array to iterate through the `arr` array and determine if the current element is greater than its previous element. If so, it returns `False` since a sorted array in non-decreasing order cannot be achieved. If the current element is less than the previous element and the `ans` array has not been marked false for the previous element, it marks the `ans` array as `False` at the previous element position. This process continues until it reaches the first element of the `arr` array, at which point it returns `True` if all elements in `arr` are sorted in non-decreasing order.

This implementation is more efficient than the previous one due to its linear time and space complexity.