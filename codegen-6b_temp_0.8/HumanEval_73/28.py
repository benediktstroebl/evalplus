
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
    # TODO: write this function

    def searchMinimum(arr, target, left, right):
        if left > right:
            return arr

        if target < arr[left]:
            return searchMinimum(arr, target, left + 1, right)
        elif target > arr[right]:
            return searchMinimum(arr, target, left, right - 1)
        else:
            return left

    def createList(arr):
        return [list(arr)]

    def smallestChange(arr):
        if len(arr) == 0:
            return 0

        end = len(arr) - 1
        start = 0

        midpoint = int(end / 2 + 1)
        while start < midpoint:
            if arr[start] == arr[end]:
                start += 1
                end -= 1
            else:
                break

        mylist = createList(arr[start:end + 1])

        if end == start:
            return 1

        temp1 = smallestChange(arr[start:end + 1])
        temp2 = smallestChange(arr[start + 1:end + 1])

        return min(temp1, temp2) + 1

    minChange = smallestChange(arr)
    return minChange
