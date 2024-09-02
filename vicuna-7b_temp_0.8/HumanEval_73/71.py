
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
    # Step 1: Create a dictionary to count the number of palindromic subarrays
    count = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                key = arr[i]
                if key not in count:
                    count[key] = 1 + count.get(key, 0)
                else:
                    count[key] += 1

    # Step 2: Find the maximum count
    max_count = max(count.values())

    # Step 3: Find the minimum number of elements that need to be changed
    min_diff = max_count
    for key in count:
        count[key] //= 2
        diff = abs(count[key] - 1)
        if diff < min_diff:
            min_diff = diff

    return min_diff
