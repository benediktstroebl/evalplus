
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
    new_arr = []
    for x in range(1,10):
        for i in arr:
            if i == x:
                new_arr.append(x)
                arr.remove(x)
    new_arr.sort(reverse=True)

    # for x in range(1, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "One"
    
    # print(new_arr)

    # for x in range(2, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Two"
    
    # print(new_arr)

    # for x in range(3, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Three"
    
    # print(new_arr)

    # for x in range(4, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Four"
    
    # print(new_arr)

    # for x in range(5, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Five"
    
    # print(new_arr)

    # for x in range(6, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Six"
    
    # print(new_arr)

    # for x in range(7, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Seven"
    
    # print(new_arr)

    # for x in range(8, 10):
    #     for i in new_arr:
    #         if i == x:
    #             i = "Eight"
    
    # print(new_arr)

    # for
