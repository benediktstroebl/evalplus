
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
    # Your code here
    # If no elements in arr are palindromic, return len(arr)
    # else:
    #     Make a string representation of arr
    #     If arr is already palindromic, return 0
    #     else:
    #         If odd number of characters, just remove the middle
    #         else:
    #             Make two palindromic substrings by removing one character in the middle
    #             Count the number of changes in each subtring
    #             Return the smallest number of changes
    if not arr:
        return 0

    string = str(arr)
    if string == string[::-1]:
        return 0
    if len(string) % 2 == 1:
        return 1

    substring1 = string[:len(string) // 2]
    substring2 = string[len(string) // 2 + 1:]
    return min(len(substring1) - palindromic(substring1), len(substring2) - palindromic(substring2))

