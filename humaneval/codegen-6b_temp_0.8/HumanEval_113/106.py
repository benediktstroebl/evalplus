
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
    def is_odd(n):
        return n % 2 != 0
    output = []
    for s in lst:
        res = 0
        s = s.replace('0',"")
        if not s:
            output.append("no digits appear ")
            continue
        for i in s:
            if is_odd(int(i)):
                res += 1
        output.append(f"the number of odd elements {res} of the str4ng {s} of the {len(lst)}n input.")
        
    return output




