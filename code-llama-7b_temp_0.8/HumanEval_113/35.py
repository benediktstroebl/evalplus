
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
    # Your code here!
    #hint: len(list_str[0])
    #hint: int(list_str[0][0])%2
    return_list=[]
    for i in lst:
        odd_number=0
        for j in i:
            if int(j)%2!=0:
                odd_number=odd_number+1
        return_list.append("the number of odd elements "+str(odd_number)+"n the str"+str(odd_number)+"ng "+str(odd_number)+" of the "+str(odd_number)+"nput.")
    return return_list
