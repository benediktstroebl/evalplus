
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
    digits = [int(d) for d in lst]
    n = len(digits)
    if n % 2 == 0:
        return ['']
    else:
        odd_count = 0
        for i in range(n):
            if odd_count < i:
                odd_count = i
        return [str(odd_count)]

lst = [
'11111',
'12345',
'1234567',
'12345678',
'11111111',
'111111111',
'1111111111',
'11111111111',
'111111111111',
'1111111111111',
'11111111111111',
'111111111111111']
