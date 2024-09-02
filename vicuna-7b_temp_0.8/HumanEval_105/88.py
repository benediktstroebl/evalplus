
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
    # check if the array is empty
    if not arr:
        return []

    # sort the array in ascending order
    arr = sorted(arr)

    # reverse the array
    arr = list(map(lambda x: x if x in "123456789" else "Unknown", arr))

    # reverse the array again
    arr = list(reversed(arr))

    result = []
    while arr:
        # check if the length of arr is greater than 1
        if len(arr) > 1:
            # get the first two elements
            first, second = arr.pop(0), arr.pop(0)

            # check if the first digit is between 1 and 9
            if first >= 1 and first <= 9:
                # get the name of the first digit
                first_name = "One"
                second_name = "Nine"
            else:
                # if the first digit is a strange number, ignore it
                first_name = ""
                second_name = "Unknown"
            first_str = str(first)

            # check if the second digit is between 1 and 9
            if second >= 1 and second <= 9:
                # get the name of the second digit
                second_name = "Two"
            else:
                # if the second digit is a strange number, ignore it
                second_name = "Unknown"
            second_str = str(second)

            # concatenate the first and second strings with the first and second names
            result.append(first_str + second_str + first_name + second_name)

        # check if the length of arr is 1
        else:
            # get the first element
            first = arr.pop(0)

            # check if the first digit is between 1 and 9
            if first >= 1 and first <= 9:
                # get the name of the first digit
                first_name = "One"
            else:
                # if the first digit is a strange number, ignore it
                first_name = "Unknown"
                first_str = str(first)

            # get the first digit
