
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

    # Initialize a dict to count occurrences of each element in the array
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Initialize a set to store the midpoint of the array
    midpoint_set = set()
    for i in range(len(arr) // 2):
        midpoint_set.add(arr[i])

    # Calculate the number of changes needed
    change_count = 0
    for num, count in count_dict.items():
        if num in midpoint_set:
            # If the midpoint element is present, it doesn't need to be changed
            continue
        elif count % 2 == 0:
            # If the element has an even count, it doesn't need to be changed
            continue
        else:
            # If the element has an odd count, it needs to be changed to match the midpoint
            change_count += 1
    return change_count
