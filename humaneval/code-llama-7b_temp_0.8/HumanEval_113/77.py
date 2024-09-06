
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
    # your code here
    lst1 = []
    for j in range(len(lst)):
        lst2 = []
        for i in lst[j]:
            lst2.append(int(i))
        c = 0
        for i in lst2:
            if i % 2 == 1:
                c += 1
        lst1.append("the number of odd elements "+str(c)+"n the str"+str(j+1)+"ng "+str(j+1)+" of the "+str(j+1)+"nput.")
    return lst1
    
