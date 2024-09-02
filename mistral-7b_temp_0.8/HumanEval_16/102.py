

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # what would be a good approach to solving this?
    # I don't think we can simply sum up the letters since we would count each
    # letter twice and the goal is to count them only once
    # maybe we could create a dictionary with unique letters as keys and the number of times
    # we find them in the string as value?
    # or a list that has letters that appear more than once and that we have to remove?
    # or maybe we could use the letters to create a list and then have a loop and when a letter
    # is different from the last one in the list, append it to the list?
    # or maybe we could use the letters to create a list and then have a loop and when a letter
    # is different from the last one in the list, append it to the list?
    # I think I prefer the last one
    # another solution would be to use an empty list and create a loop that compares the first letter
    # with each letter in the string and when they are different, append the first letter to the list
    # and set it as the new first letter and then continue the loop
    # I
