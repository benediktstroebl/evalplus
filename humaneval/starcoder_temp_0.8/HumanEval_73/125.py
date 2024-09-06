
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
    # This is a very nice O(n) solution
    # 1. Find the element with the largest number of consecutive duplicates
    # 2. Calculate the amount of elements to change by subtracting the number of duplicates
    # from the number of non-duplicates
    # 3. Return the number of elements to change
    arr = [0] + arr + [0]
    # edge case
    if arr == [0]:
        return 0
    # Count non-duplicates and duplicates
    counter = Counter(arr)
    max_num = max(counter.values())
    duplicates = [k for k, v in counter.items() if v == max_num]
    # If an even number of elements are non-duplicates, the min. number of elements to change
    # is the sum of the duplicates
    if len(duplicates) % 2 == 0:
        return sum(duplicates)
    # If an odd number of elements are non-duplicates, the min. number of elements to change
    # is the sum of the duplicates minus the single element with the most duplicates
    else:
        return sum(duplicates) - max_num

