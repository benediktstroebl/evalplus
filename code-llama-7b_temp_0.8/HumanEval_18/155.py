

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # check if the substring exists in the string
    if not string:
        return 0
    if not substring:
        return 0
    if substring not in string:
        return 0

    # get the list of indexes of the substring in the string
    list_of_substring_indexes = []
    substring_index = 0
    while True:
        substring_index = string.find(substring, substring_index)
        if substring_index == -1:
            break
        list_of_substring_indexes.append(substring_index)
        substring_index += 1

    # get the indexes of the different substrings of the substring
    sub_substrings_indexes = []
    for i in range(len(substring)):
        for j in range(i + 1, len(substring) + 1):
            sub_substrings = substring[i:j]
            sub_substrings_indexes.append(sub_substrings)

    # for each sub_substring, get the number of occurrences
    n = len(substring)
    n_occurrences = 0
    for sub_substring in sub_substrings_indexes:
        if len(sub_substring) < n:
            continue
        # check that it is a sub_substring and not a different string
        if sub_substring not in string:
            continue
        # check that it is not the original substring
        if sub_substring == substring:
            continue
        for sub_substring_index in list_of_substring_indexes:
            if string[sub_substring_index:sub_substring_index + n] == sub_substring:
                n_occurrences += 1

    return n_occurrences

