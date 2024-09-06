
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
    # n = len(arr)
    # new_arr = []
    #
    # if n == 0:
    #     return []
    #
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if arr[i] < arr[j] and 1 <= arr[i] <= 9:
    #             new_arr.append(arr[i])
    #         elif arr[i] > arr[j] and 1 <= arr[j] <= 9:
    #             new_arr.append(arr[j])
    #     if arr[i] < 10 and arr[i] > 0:
    #         new_arr.append(arr[i])
    # return new_arr


    def names(arr):
        return [
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine"
        ]

    return [names(arr)[i-1] for i in sorted(arr) if i in range(1, 10)]

