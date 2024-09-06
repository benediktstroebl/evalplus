
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    #
    # LINEAR SEARCH: O(n)
    #
    # sorted_arr = sorted(arr, reverse=True)
    # return [digit_to_name(digit) for digit in sorted_arr]
    #

    #
    # BINARY SEARCH: O(n log n)
    #
    # sorted_arr = sorted(arr)
    # return [digit_to_name(digit) for digit in sorted_arr[::-1]]
    #

    #
    # BINARY SEARCH VERSION 2: O(n log n)
    #
    # digit_to_name_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    #                       6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    #
    # sorted_arr = sorted(arr)
    # return [digit_to_name_dict[digit] for digit in sorted_arr[::-1]]
    #

    #
    # BINARY SEARCH VERSION 3: O(n)
    #
    digit_to_name_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                          6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    def digit_to_name(digit):
        for key, value in digit_to_name_dict.items():
            if key == digit:
                return value
        return None

    def binary_search(arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

    sorted_arr = sorted(
