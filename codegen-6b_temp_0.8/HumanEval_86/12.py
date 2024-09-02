
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    def get_asc(str):
        asc = []
        for e in str:
            asc.append(ord(e))
        return asc
    
    def get_sort(asc):
        sort_asc = sorted(asc)
        sort_str = []
        for e in sort_asc:
            sort_str.append(chr(e))
        return ''.join(sort_str)

    return get_sort(get_asc(s)) if s else s

        
    
