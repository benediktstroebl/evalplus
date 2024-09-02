
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
    #remove spaces
    for i in range(0,len(lst)):
        while " " in lst[i]:
            lst[i].replace(" ","")
    #create a dictionary with the key as the index of the element and the value
    #as the number of odd digits in the element
    d = {}
    for i in range(len(lst)):
        n = []
        for j in range(len(lst[i])):
            n.append(int(lst[i][j]))
        d[i]=n.count(1)
    #create a list with each element as a string of the form
    #"the number of odd elements in the string i of the input"
    l = []
    for i in range(len(d)):
        l.append(f"the number of odd elements {d[i]}n the str{i}ng {i} of the {i}nput.")
    return l
