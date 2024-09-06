
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

    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def reverse(arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            swap(arr, left, right)
            left += 1
            right -= 1
        return arr

    def digit_to_string(d):
        if d == 0:
            return "Zero"
        elif d == 1:
            return "One"
        elif d == 2:
            return "Two"
        elif d == 3:
            return "Three"
        elif d == 4:
            return "Four"
        elif d == 5:
            return "Five"
        elif d == 6:
            return "Six"
        elif d == 7:
            return "Seven"
        elif d == 8:
            return "Eight"
        elif d == 9:
            return "Nine"

    def filter_number(num):
        if num < 1 or num > 9:
            raise Exception("Num must be between 1 and 9")
        return num

    def get_digit(num, digit):
        return (num // (10**digit)) % 10

    def digit_to_string_recur(d):
        if d < 0:
            return "Zero"
        elif d == 0:
            return "Zero"
        elif d == 1:
            return "One"
        elif d == 2:
            return "Two"
        elif d == 3:
            return "Three"
        elif d == 4:
            return "Four"
        elif d == 5:
            return "Five"
        elif d == 6:
            return "Six"
        elif d == 7:
            return "Seven"
        elif d == 8:
            return "Eight"
        elif d == 9:
            return "Nine"

    # solution 1
    # time complexity:
