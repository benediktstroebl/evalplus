def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    including overlapping occurrences.
    """ 
    def count_overlapping(text, pattern):
        i, j = 0, 0
        count = 0
        while i < len(text) - 1:
            if text[i] == pattern:
                if j == len(pattern) - 1: count += 1
                j = 0
            else:
                j += 1
            i += 1
        return count
            
    string = "aaaaaa" + "aa" + "aaa" + "a" + "a"
    substring = "aa"
    return count_overlapping(string, substring)