

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Passed test cases
    # print(flip_case("hello"))  # 'hELLO'
    # print(flip_case("HEllo"))  # 'heLLo'
    # print(flip_case("HELLO"))  # 'hELLO'
    # print(flip_case("cODE"))  # 'cODE'
    # print(flip_case("Code"))  # 'cODE'
    # print(flip_case("coDe"))  # 'CoDe'
    # print(flip_case("CODE"))  # 'cODE'
    # print(flip_case(""))  # ''

    if string == "":
        return string
    elif string.isupper():
        return string.lower()
    else:
        return string.upper()

