
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # My and best solutions
    def my_solution(s, n):
        if s == '':
            return []
        return [item for item in s.split() if sum(1 for char in item if char.isalpha() and char not in 'aeiou') == n]

    def best_solution(s, n):
        if not s:
            return []
        return [x for x in s.split() if len(x) - sum(x.count(y) for y in 'aeiou') == n]
    
    # Someone else solutions
    def fastest_solution(s, n):
        if not s:
            return []
        return [x for x in s.split() if len(x.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')) == n]

    def easiest_solution(s, n):
        return [word for word in s.split() if len(word) - sum(1 for c in word if c.lower() in "aeiou") == n]

    return my_solution, best_solution, fastest_solution, easiest_solution
