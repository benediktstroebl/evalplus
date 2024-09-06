
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

    # sort the array
    # reverse the array
    # transform the integers to words
    # return the words

    # Converting the words into numbers:
    # "One" -> 1
    # "Two" -> 2
    # "Three" -> 3
    # "Four" -> 4
    # "Five" -> 5
    # "Six" -> 6
    # "Seven" -> 7
    # "Eight" -> 8
    # "Nine" -> 9

    # Getting the words from the numbers:
    # 1 -> "One"
    # 2 -> "Two"
    # 3 -> "Three"
    # 4 -> "Four"
    # 5 -> "Five"
    # 6 -> "Six"
    # 7 -> "Seven"
    # 8 -> "Eight"
    # 9 -> "Nine"

    words_to_numbers = {"One": 1,
                        "Two": 2,
                        "Three": 3,
                        "Four": 4,
                        "Five": 5,
                        "Six": 6,
                        "Seven": 7,
                        "Eight": 8,
                        "Nine": 9}

    # Creating a list of words:
    result = []

    # Checking if array is empty or has any strange numbers:
    if len(arr) == 0 or any(i < 1 or i > 9 for i in arr):
        return result

    # Sorting the array:
    arr.sort()

    # Reversing the array:
    arr.reverse()

    # Transforming the integers to words and adding them to the result array:
    for i in arr:
        if i in words_to_numbers:
            result.append(words_to_numbers[str(i)])

    # Converting the numbers into words:
    result = [str(i) for i in result]

    # Returning the final result:
    return result
