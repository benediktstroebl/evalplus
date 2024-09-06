def cycpattern_check(first, second):
    return second in rotated_substrings(first)
def rotated_substrings(string):
    substrings = [string[i:] for i in range(len(string) + 1)]
    substrings += [string[:i] for i in range(1, len(string) + 1)]
    return substrings