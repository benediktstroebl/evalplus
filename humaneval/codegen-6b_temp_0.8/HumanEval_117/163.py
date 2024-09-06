
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
    if s.count(" ") == len(s):
        return []
    return "".join(x[0] for x in re.findall(r'\w{%d}' % n, s)).split()

test(select_words, ["Mary had a little lamb", "Mary had a little cat", "Mary had a little mouse", "Mary had a bit of a lamb", "Mary had a little lamb", "Mary had a little cat", "Mary had a little mouse", "Mary had a little lamb", "Mary had a little cat", "Mary had a little mouse", "Mary had a little lamb", "Mary had a little cat", "Mary had a little mouse", "Mary had a little lamb", "Mary had a little cat", "Mary had a little mouse", "Mary had a little lamb", "Mary had a few cat", "Mary had a few mouse", "Mary had a few lamb", "Mary had a few cat", "Mary had a few mouse", "Mary had a few lamb", "Mary had a few cat", "Mary had a few mouse", "Mary had a few lamb"], [])
test(select_words, ["simple white space", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one two two three", "four", "one