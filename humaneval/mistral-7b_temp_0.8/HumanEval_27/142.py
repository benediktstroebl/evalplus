

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_case_chars = list("abcdefghijklmnopqrstuvwxyz")
    upper_case_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_case_str = ''.join([chr(i) for i in lower_case_chars])
    upper_case_str = ''.join([chr(i) for i in upper_case_chars])
    string = list(string)
    for i in range(len(string)):
        if string[i] in lower_case_str:
            string[i] = upper_case_str[lower_case_str.index(string[i])]
        elif string[i] in upper_case_str:
            string[i] = lower_case_str[upper_case_str.index(string[i])]
    return ''.join(string)

