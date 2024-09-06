
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
    #  1.  Initial values
    n = 9                          # n > 0
    arr.sort()                     # sort the array
    arr.reverse()                  # reverse the array
    output = []

    #  2.  Looping through the array
    #      2.1  Check if the number is between 1 and 9 (inclusive)
    #      2.2  If true, add the string to the output array
    #      2.3  If false, ignore it
    for element in arr:
        if 1 <= element <= 9:
            output.append(str(element))

    #  3.  Convert the string in the output array to integers
    #      3.1  Loop through the output array
    #      3.2  Convert the string to the corresponding integer
    #      3.3  Replace the string with the integer
    for i in range(len(output)):
        output[i] = int(output[i])
        output[i] = output[i] - 1
        output[i] = output[i] + 1

    #  4.  Convert the integers in the output array to strings
    #      4.1  Loop through the output array
    #      4.2  Convert the integer to a string
    #      4.3  Replace the integer with the string
    for i in range(len(output)):
        output[i] = str(output[i])

    #  5.  Return the output array
    return output

