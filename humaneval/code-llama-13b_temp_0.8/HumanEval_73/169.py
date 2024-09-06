
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
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0
    elif arr == arr[::-1]:
        return 0

    # create a dictionary to count the number of occurences of each number
    count = dict()
    for el in arr:
        if el not in count:
            count[el] = 0
        count[el] += 1

    # initiate count of swaps
    swaps = 0
    # initiate swapped elements
    swapped = set()

    # check the odd positions in the array
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr) - 1 - i] and (arr[i] in count and arr[len(arr) - 1 - i] in count):
            if (arr[i] in count and count[arr[i]] > 0) or (arr[len(arr) - 1 - i] in count and count[arr[len(arr) - 1 - i]] > 0):
                swaps += 1
                # add the swapped elements to the set
                swapped.add(arr[i])
                swapped.add(arr[len(arr) - 1 - i])

    # check the even positions in the array
    if len(arr) % 2 == 0:
        if (arr[len(arr) // 2] in count and arr[len(arr) - 1 - (len(arr) // 2)] in count):
            if (arr[len(arr) // 2] in count and count[arr[len(arr) // 2]] > 0) or (arr[len(arr) - 1 - (len(arr) // 2)] in count and count[arr[len(arr) - 1 - (len(arr) // 2)]] > 0):
                swaps += 1
                # add the swapped elements to the set
                swapped.add(arr[len(arr) // 2])
                swapped.add(arr[len(arr) - 1 - (len(arr)
