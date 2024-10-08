
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
    # arr = [2, 1, 1, 4, 5, 8, 2, 3]
    # arr = []
    # arr = [1, -1 , 55]
    result = []

    # for i in range(len(arr)):
    #     if 1 <= arr[i] <= 9:
    #         result.append(arr[i])

    for num in arr:
        if 1 <= num <= 9:
            result.append(num)
    
    result = sorted(result, reverse = True)
    # for i in range(len(result)):
    #     if 1 <= result[i] <= 9:
    #         result[i] = f'One' if result[i] == 1 else f'Two' if result[i] == 2 else f'Three' if result[i] == 3 else f'Four' if result[i] == 4 else f'Five' if result[i] == 5 else f'Six' if result[i] == 6 else f'Seven' if result[i] == 7 else f'Eight' if result[i] == 8 else f'Nine' if result[i] == 9 else result[i]

    # 1: One
    # 2: Two
    # 3: Three
    # 4: Four
    # 5: Five
    # 6: Six
    # 7: Seven
    # 8: Eight
    # 9: Nine

    for i in range(len(result)):
        result[i] = f'One' if result[i] == 1 else f'Two' if result[i] == 2 else f'Three' if result[i] == 3 else f'Four' if result[i] == 4 else f'Five' if result[i] == 5 else f'Six' if result[i] == 6 else f'Seven' if result[i] == 7 else f'Eight' if result[i] == 8 else f'Nine' if result[i] == 9 else result[i]
