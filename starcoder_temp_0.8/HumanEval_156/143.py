
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

    # write your answer between #start and #end
    #start
    roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    numbers = [roman_dict[x] for x in list(roman_dict.keys())]
    numbers.sort(reverse=True)
    result = []
    for num in numbers:
        while number >= num:
            result.append(roman_dict.keys()[roman_dict.values().index(num)])
            number -= num
    #end
    return "".join(result)
