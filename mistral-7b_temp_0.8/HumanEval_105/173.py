
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
    return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    def check(arr, i):
        try:
            if arr[i] < 1 or arr[i] > 9:
                return False
            else:
                return True
        except IndexError:
            return False
        
        def sort_by_length(arr):
        length = 0
        for i in range(len(arr)):
            if check(arr, i):
                length += 1
                arr.sort(key=lambda x: len(str(x)))
                arr = arr[length:]
    
            def reverse(arr):
        length = len(arr)
        for i in range(length // 2):
            arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]
    
            def names_of_numbers(arr):
        result = []
        for i in arr:
            if check(
