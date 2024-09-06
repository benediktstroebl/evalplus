
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
    def count_change(arr, change):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] != arr[j]:
                    count += 1
                    break
        return count
    
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[left] != arr[mid]:
            if count_change(arr, mid) < count_change(arr, mid+1):
                arr[left], arr[mid] = arr[mid], arr[left]
                arr[mid+1], arr[right] = arr[right], arr[mid+1]
                count_change(arr, mid)
                count_change(arr, mid+1)
                left = mid + 1
                right = len(arr) - 1
        else:
            right = mid - 1
    return left
