
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

    def sort_numbers(arr):
        arr.sort()
        return arr

    def reverse_numbers(arr):
        length = len(arr) - 1
        for i in range(len(arr) // 2):
            arr[i], arr[length - i] = arr[length - i], arr[i]
        return arr

    def digit_to_name(digit):
        """
        digit: int
        return the name of the digit (string)
        """
        if digit == 1:
            return "One"
        elif digit == 2:
            return "Two"
        elif digit == 3:
            return "Three"
        elif digit == 4:
            return "Four"
        elif digit == 5:
            return "Five"
        elif digit == 6:
            return "Six"
        elif digit == 7:
            return "Seven"
        elif digit == 8:
            return "Eight"
        elif digit == 9:
            return "Nine"
        return "One"

    def transform_list(arr):
        """
        arr: array of numbers between 1 and 9 (inclusive)
        return an array of names (strings)
        """
        new_list = []
        for i in arr:
            new_list.append(digit_to_name(i))
        return new_list

    def filter_list(arr):
        """
        arr: array of integers
        return a new array containing only the numbers that are between 1 and 9 inclusive.
        """
        new_list = []
        for i in arr:
            if 1 <= i <= 9:
                new_list.append(i)
        return new_list

    arr = filter_list(arr)
    arr = sort_numbers(arr)
    arr = reverse_numbers(arr)
    return transform_list(arr)

