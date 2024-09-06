
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
    
    def convert_to_palindrome(arr):
        """
        Given an array arr, rearranges the elements in new_arr so that 
        it forms a palindrome. If an array is already palindrome, do nothing.
        """
        new_arr = []
        for i in arr:
            if i not in new_arr:
                new_arr.append(i)
        if len(new_arr) % 2 == 0:
            return new_arr
        else:
            for i in new_arr[:len(new_arr)//2]:
                new_arr.append(i)
            for i in new_arr[len(new_arr)//2]:
                new_arr.append(i)
        return new_arr

    arr_len = len(arr)
    arr = convert_to_palindrome(arr)
    if len(arr) % 2 == 0:
        return (arr_len - len(arr))//2
    else:
        return (arr_len - len(arr))//2 + (arr_len - len(arr))%2


