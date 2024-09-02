
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
    # Write your code here.

    # https://www.geeksforgeeks.org/count-palindromic-substrings-set-1/

    def countPalindrome(arr, start, end):
        count = 0
        for i in range(start, end):
            if arr[i] == arr[end-i]:
                count += 1
        return count

    def makePalindrome(arr):
        count = 0
        length = len(arr)
        for i in range(length-1):
            for j in range(length-1):
                if arr[i] == arr[j]:
                    if countPalindrome(arr, i, j) == (j-i+1)//2:
                        count += 1
                        for k in range(i+1, j+1):
                            arr[k] = arr[length-1-k]
        return count

    print(makePalindrome(arr))
