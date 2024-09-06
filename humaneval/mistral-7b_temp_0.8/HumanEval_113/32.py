
def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    # For each digit in each string
    #     If the digit is odd
    #         Increment a variable
    #     Else
    #         Decrement a variable
    # Return the value of the variable
    # Raise a ValueError if any element of the input is not a string
    #     (which is a value error)
    # Raise a ValueError if any element of the input is not a string
    #     (which is a value error)
    if not isinstance(lst,list) or not all(isinstance(i,str) for i in lst):
        raise ValueError("Type of input is not a list of strings")
    # For each element in the input
    #     If element is not a string
    #         raise a value error
    # Raise a ValueError if any element of the input is not a string
    #     (which is a value error)
    for i in lst:
        if not isinstance(i,str):
            raise ValueError("Input contains non string elements")
    # For each element in the input
    #     Create a variable that counts the number of odd elements
    
