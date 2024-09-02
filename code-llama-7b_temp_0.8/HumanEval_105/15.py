
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
    # Your code here
    # replace each digit by its corresponding name from
    # "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    # if the number is 1 - 9, replace it
    # otherwise, if the number is not between 1 and 9, leave it as it is
    # but if it is between 1 and 9, replace it with its name
    # ex: if number is 1, replace it with "One"
    # if number is 2, replace it with "Two"
    # if number is 3, replace it with "Three"
    # if number is 4, replace it with "Four"
    # if number is 5, replace it with "Five"
    # if number is 6, replace it with "Six"
    # if number is 7, replace it with "Seven"
    # if number is 8, replace it with "Eight"
    # if number is 9, replace it with "Nine"
    # all numbers between 1 and 9 will be replaced
    # all numbers that are not between 1 and 9 will be left as it is
    # ex: 1,2,1,3,5,1,10,1,99,1,3,4,6,1,2
    # ex: 1,1,2,2,3,4,5,8,2,3
    # ex: -1,1,55
    # if the number is not between 1 and 9, leave it as it is
    # if the number is between 1 and 9, replace it with its name
    # ex: 1,2,1,3,5,1,10,1,99,1,3,4,6,1,2
    # ex: 1,1,2,2,3,4,5,8,2,3
    # ex: -1,1,55
    # ex: 1,2,1,3,5,1,10,1,99,1,3,4,6,1,2
    #
