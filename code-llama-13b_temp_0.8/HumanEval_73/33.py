
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
    if len(arr) < 2:
        return 0

    if len(arr) == 2:
        return 1

    if arr[0] != arr[-1]:
        return 1

    # store in a dict the positions for each number
    d = dict()

    for i, num in enumerate(arr):
        if num not in d:
            d[num] = [i]
        else:
            d[num].append(i)

    count = 0

    for num in d:
        if len(d[num]) == 1:
            continue

        if len(d[num]) % 2 == 0:
            # even
            for i in range(0, len(d[num]), 2):
                # swap the position in pairs
                arr[d[num][i]], arr[d[num][i + 1]] = arr[d[num][i + 1]], arr[d[num][i]]
                count += 1
        else:
            # odd
            for i in range(1, len(d[num]), 2):
                # swap the position in pairs
                arr[d[num][i]], arr[d[num][i - 1]] = arr[d[num][i - 1]], arr[d[num][i]]
                count += 1

    return count

