
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
    # TODO: Create a list to hold the count of odd elements of each string
    result=[]
    # TODO: Iterate through the list of strings
    for i in lst:
        # TODO: Create a count variable to keep track of the number of odd digits in the string
        count=0
        # TODO: Iterate through the digits of the string
        for j in i:
            # TODO: If the digit is odd, increment the count
            if(int(j)%2==1):
                count+=1
        # TODO: Add the count of odd digits to the result list
        result.append("the number of odd elements in the string {} of the input. ".format(count))
    return result
