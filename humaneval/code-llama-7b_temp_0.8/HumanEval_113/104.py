
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
    #creating list to store the odd number of elements in the strings
    result=[]
    #going through each string
    for s in lst:
        #setting counter to zero for each string
        odd_count=0
        #counting the number of odd numbers in the string
        for i in s:
            if int(i)%2!=0:
                odd_count=odd_count+1
        #appending the number of odd numbers in the string to the list
        result.append("the number of odd elements "+str(odd_count)+"n the str"+str(odd_count)+"ng "+str(odd_count)+" of the "+str(odd_count)+"nput.")
    return result



