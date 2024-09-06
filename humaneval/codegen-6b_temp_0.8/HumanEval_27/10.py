

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # # BEST:
    # return string.swapcase()
    #
    # #ONEYEAR
    # lower = [chr(ord(ch) + 32) if ch.isupper() else ch for ch in string]
    # upper = [chr(ord(ch) - 32) if ch.islower() else ch for ch in string]
    # return ''.join(lower + upper)
    #
    # # ONEYEAR MUSK
    # return ''.join([''.join([chr(ord(ch) + 32) if ch.islower() else chr(ord(ch) - 32) if ch.isupper() else ch for ch in string[i:i + 2]]) for i in range(0, len(string), 2)])
    #
    # #TWOYEAR
    # return ''.join([chr(ord(ch) - 32) if ch.islower() else chr(ord(ch) + 32) if ch.isupper() else ch for ch in string])
    #
    # #MYFELIX
    # result = []
    # for i in range(len(string)):
    #     c = string[i]
    #     if c.isupper(): c = c.lower()
    #     elif c.islower(): c = c.upper()
    #     result.append(c)
    # return ''.join(result)
    #
    # #Y2020
    # l = len(string)
    # result = []
    # for i in range(int(l / 2)):
    #     result.append(string[l - i - 1])
    #     result.append(string[i])
    #     result.append(string[i])
    # if l % 2:
    #     result.append(string[l - 1])
    # return ''.join(result)

    # #SINF
    # result = []
    # for i in range(len(string)):
    #     if string[i].isupper():
    #         result.append(string[i].lower())
    #     elif string[i].islower():
    #         result.