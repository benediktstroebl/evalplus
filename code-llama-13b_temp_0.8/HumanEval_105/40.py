
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

    # Create a new dictionary that maps a number to its name
    name_dict = {
        1 : 'One',
        2 : 'Two',
        3 : 'Three',
        4 : 'Four',
        5 : 'Five',
        6 : 'Six',
        7 : 'Seven',
        8 : 'Eight',
        9 : 'Nine'
    }
    
    # Create an empty list that will hold the numbers mapped to their names
    num_names = []
    
    # Create an empty list that will hold the numbers that are between 1 and 9
    num_list = []
    
    # for each number in the given array:
    for number in arr:
        # if the number is between 1 and 9:
        if number > 0 and number <= 9:
            # append the number to the list of numbers that are between 1 and 9
            num_list.append(number)

    # sort the list of numbers that are between 1 and 9
    num_list.sort()
    # reverse the list of numbers that are between 1 and 9
    num_list.reverse()
    
    # for each number in the list of numbers that are between 1 and 9
    for number in num_list:
        # get the name of the number and append it to the list of numbers mapped to their names
        num_names.append(name_dict[number])
        
    # return the list of numbers mapped to their names
    return num_names

