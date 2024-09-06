
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_list = ['iv', 'v', 'x', 'l', 'c', 'd', 'm']
    roman_dict = {'i':1, 'v':5, 'x':10, 'l':50, 'c':100, 'd':500, 'm':1000}
    result = ''
    num_str = str(number)
    for i in range(len(num_str)):
        for ch in roman_list:
            if num_str[i] == ch[0]:
                if i == len(num_str) - 1:
                    result += ch * roman_dict[ch[0]]
                elif num_str[i+1] == ch[1]:
                    result += ch * roman_dict[ch[0]]
                elif num_str[i+1] != ch[1]:
                    result += ch * roman_dict[ch[0]]
                    break

    return result
