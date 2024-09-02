
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

    def palindromic(arr):
        # Create an array that holds the count of each number in arr
        count = [0] * 10
        for num in arr:
            count[num] += 1
        odds = []
        for i in range(1, 10):
            if count[i] % 2 == 1:
                odds.append(i)
        return odds
    odds = palindromic(arr)
    # The number of odd numbers is odd
    if len(odds) % 2 == 1:
        return -1
    # The number of odd numbers is even
    else:
        return len(odds) // 2
