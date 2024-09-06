

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # set the value of the counter to 0
    count = 0
    # set the value of the substring_index to 0
    substring_index = 0
    # loop through the string
    for char in string:
        # if the character at the current index matches the first character of the substring
        if char == substring[substring_index]:
            # if the substring_index is equal to the length of the substring minus 1
            if substring_index == len(substring) - 1:
                # increment the counter
                count += 1
                # reset the substring_index to 0
                substring_index = 0
            # if the substring_index is not equal to the length of the substring minus 1
            else:
                # increment the substring_index
                substring_index += 1
        # if the character at the current index does not match the first character of the substring
        else:
            # reset the substring_index to 0
            substring_index = 0
    # return the value of the counter
    return count

