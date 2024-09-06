
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    # create a hash table and insert the keys into it
    ht = {}
    for i in range(n):
        ht[arr[i]] = i
    # now traverse the array from the last element to the first element
    # and maintain a counter variable for tracking the changes
    count = 0
    for i in range(n-1,-1,-1):
        if arr[i] != arr[i+1]:
            # if the current and the next element are not equal,
            # we need to change the current element to make it palindromic
            # so we increment the counter
            count += 1
        # now we look up the index of the next element in the hash table
        # and store it in temp variable
        temp = ht[arr[i+1]]
        # now we find the position of the current element in the hash table
        # and replace it with the index of the next element
        ht[arr[i]] = temp
    return count
