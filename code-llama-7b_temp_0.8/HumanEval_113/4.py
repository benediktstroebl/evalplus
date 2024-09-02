
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
    list_of_strings = []
    #for each item in the list of strings
    for item in lst:
        string = ""
        #check if odd or even
        num_of_odd_elems = 0
        #for each char in item
        for num in item:
            #check if odd
            if int(num) % 2 != 0:
                num_of_odd_elems += 1
        #if odd append string with number of odd chars and item
        string = "the number of odd elements " + str(num_of_odd_elems) + "n the str" + item + "ng " + str(num_of_odd_elems) + "n the 8nput."
        list_of_strings.append(string)
    return list_of_strings
