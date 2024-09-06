
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
    odd_counts = []
    for i in range(0,len(lst)):
        string = lst[i]
        num_odd = 0
        for j in range(0,len(string)):
            if string[j] == '1' or string[j] == '3' or string[j] == '5' or string[j] == '7' or string[j] == '9':
                num_odd += 1
        string = string.replace(string[i],str(num_odd))
        odd_counts.append(string)
    return odd_counts
