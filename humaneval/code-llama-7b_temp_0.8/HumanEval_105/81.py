
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
    # what's the best way to handle the empty arr?
    
    # what's the best way to handle the strange numbers?
    # do we want to catch the error and then ignore it?
    # do we want to handle it ahead of time and filter it out?
    # what is the best way to filter it out?
    # should we use an if statement?
    # should we use a list comprehension?
    # should we use a map function?
    
    # what's the best way to reverse the array?
    # should we use the reversed function?
    # should we use a for loop and slice the array?
    # should we use a list comprehension?
    
    # what's the best way to transform digits to words?
    # should we create a dictionary?
    # should we use a map function?
    # should we use a list comprehension?
    return list(map(lambda n: {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}[str(n)], sorted(arr, reverse=True)))

