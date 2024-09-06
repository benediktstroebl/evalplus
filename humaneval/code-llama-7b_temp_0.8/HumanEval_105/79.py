
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
    if len(arr) == 0:
        return []
    else:
        arr_of_digits = [int(i) for i in arr if int(i) < 10 and int(i) > 0]
        new_arr = []
        for i in range(len(arr_of_digits)):
            new_arr.append(str(arr_of_digits[i]))
        new_arr.sort()
        new_arr.reverse()
        answer = []
        for i in new_arr:
            if i == "1":
                answer.append("One")
            if i == "2":
                answer.append("Two")
            if i == "3":
                answer.append("Three")
            if i == "4":
                answer.append("Four")
            if i == "5":
                answer.append("Five")
            if i == "6":
                answer.append("Six")
            if i == "7":
                answer.append("Seven")
            if i == "8":
                answer.append("Eight")
            if i == "9":
                answer.append("Nine")
        return answer
