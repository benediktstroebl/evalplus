def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    return len(set(string.upper())) 


# -------- Part 4: Implementing Backtracking -------------------------------------------------------
# Our goal is to find the shortest string that has nCS characters. There are a few rules to follow:
# 1. Given a sequence of C characters, any character that appears more than once must be an equal number of times. We only need to count once to determine the length of this sequence.
# 2. Given a string S, find out how many CS characters it consists of - given CS characters in a string, we need to take into account that we don't have to worry about permutations - and only care about the longest possible permutation.
# 3. We only need to consider longer sequences than our longest sequences until we reach the end of the string. Remember that we are looking for CS characters in a string, so we start off by considering any character that appears once.
# 4. Once we reach the end of the string, we know the string consists of CS characters because when we consider longer sequences of characters, we can stop considering longer sequences and only consider shorter sequences.
# 5. If the longest sequence of characters doesn't contain CS characters, return -1
# 6. Else return the length of this longest sequence.

# Our solution starts by counting the number of CS characters before we start considering longer sequences of characters and then counting how many CS characters we may have after that without considering longer sequences. We then continue to count the CS characters in the longest sequences until we reach the end of the string without considering longer sequences. Note that we must check for a null string before continuing. We also must check that the string does not contain any duplicate characters.

