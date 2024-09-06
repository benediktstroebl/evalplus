
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
    if not arr:
        return []

    # 1. find all numbers between 1 to 9
    valid_nums = [num for num in arr if 1 <= num <= 9]
    # 2. sort the valid numbers
    valid_nums = sorted(valid_nums)
    # 3. reverse the valid numbers
    valid_nums = valid_nums[::-1]
    # 4. make it all string
    valid_nums = [str(num) for num in valid_nums]
    # 5. get each number from the valid numbers
    valid_nums = [f"{num}" for num in valid_nums]
    # 6. replace each number with corresponding name
    valid_nums = [["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][int(num) - 1] for num in valid_nums]
    # 7. return the valid numbers as list
    return valid_nums

