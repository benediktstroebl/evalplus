
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
    return [f"the number of odd elements {sum([int(i)%2!=0 for i in str(j)])}n the str{sum([int(i)%2!=0 for i in str(j)])}ng {sum([int(i)%2!=0 for i in str(j)])} of the {sum([int(i)%2!=0 for i in str(j)])}nput." for j in lst]


    # def odd_count(lst):
    #     res = []
    #     for i in lst:
    #         counter = 0
    #         for j in i:
    #             if int(j) % 2 != 0:
    #                 counter += 1
    #         res.append(f"the number of odd elements {counter}n the str{counter}ng {counter} of the {counter}nput.")
    #     return res

    # def odd_count(lst):
    #     return [f"the number of odd elements {sum([int(i)%2!=0 for i in str(j)])}n the str{sum([int(i)%2!=0 for i in str(j)])}ng {sum([int(i)%2!=0 for i in str(j)])} of the {sum([int(i)%2!=0 for i in str(j)])}nput." for j in lst]
