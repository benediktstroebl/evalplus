
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

    def valid_palindromic_array(arr):
        """
        Checks if the array is a palindromic array
        """
        return arr == arr[::-1]

    def palindromic_change(arr):
        """
        Finds the minimum number of elements that need to be changed to make the array a palindromic array
        """
        arr = arr.copy()
        palindromic = valid_palindromic_array(arr)

        if palindromic:
            return 0

        while not palindromic:
            # Loop over each element and change to any other element
            for i in range(len(arr)):
                arr[i] = (arr[i] + 1) % 10

            palindromic = valid_palindromic_array(arr)
            if palindromic:
                break
        
        return len(arr) - len(arr[::-1])

    return palindromic_change(arr)
