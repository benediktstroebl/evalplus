
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
    changes_required = 0
    current_palindrome = arr.copy()
    for i in range(len(arr)):
        current_element = arr[i]
        index = len(current_palindrome) - 1
        for _ in range(index, 0, -1):
            if current_palindrome[index] <= current_element:
                index -= 1
                continue
            elif current_palindrome[index] > current_element:
                current_palindrome[index] = current_element
                changes_required += 1
                break
    return changes_required

