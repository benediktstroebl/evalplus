
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
    if not arr:
        return 0

    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1

    # we need to find the smallest change to turn the given array into a palindrome
    # first step is to find the first occurance of an item,
    # and the last occurance of the same item
    #
    # this method will find the first occurance of an item, and the last occurance of the same item
    # the return is a tuple of the two indexes
    def find_occurance_of_item(item, list_of_items):
        try:
            first = list_of_items.index(item)
        except Exception as e:
            first = None

        try:
            second = list_of_items[::-1].index(item)
        except Exception as e:
            second = None

        if first == None and second == None:
            return None

        if second == None:
            second = len(list_of_items) - 1

        if first == None:
            first = 0

        return (first, second)

    def find_smallest_change(arr):
        # find the first occurance of an item, and the last occurance of the same item
        first_occurance = find_occurance_of_item(arr[0], arr)
        last_occurance = find_occurance_of_item(arr[-1], arr)

        # if neither the first or last occurance are none, then just flip the first and last item
        if first_occurance != None and last_occurance != None:
            return 1

        # remove all occurances of the first item, and then check the list again
        # if the item that is left is a palindrome, then we can remove the rest of the items
        # and it will still be a palindrome
        if first_occurance != None:
            arr = arr[:first_occurance[0]] +
