
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

    # SOLUTION 1:
    # lst_out = []
    # for idx in range(len(lst)):
    #     count = 0
    #     for char in lst[idx]:
    #         if int(char) % 2 != 0:
    #             count += 1
    #     lst_out.append(f"the number of odd elements in the string {count} of the input.")
    # return lst_out

    # SOLUTION 2:
    # lst_out = []
    # for idx in range(len(lst)):
    #     lst_out.append(f"the number of odd elements in the string {sum([int(i) % 2 != 0 for i in lst[idx]])} of the input.")
    # return lst_out

    # SOLUTION 3:
    return [f"the number of odd elements in the string {sum([int(i) % 2 != 0 for i in lst[idx]])} of the input." for idx in range(len(lst))]
