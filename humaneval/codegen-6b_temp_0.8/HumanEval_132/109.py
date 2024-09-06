
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    # I can iterate over the string without any side effects.
    string = list(string)
    counts = [0] * len(string) # (O(n))

    def helper(left, right):
        if left >= right:
            return True
        for i in range(left, right):
            if string[i] == '[':
                counts[left] += 1

            if string[i] == ']':
                counts[left] -= 1

            if string[i] == '[' and counts[left] < 0:
                return False

            if string[i] == ']' and counts[left] >= 0:
                return False

            if string[i] == '[' or string[i] == ']':
                if helper(left, i):
                    return True
            else:
                continue

            if string[i] == ']' and counts[left] >= 0:
                return True

        return False

    return helper(0, len(counts))


import unittest
