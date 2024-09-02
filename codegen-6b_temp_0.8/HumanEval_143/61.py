
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    s = sentence.split()
    n = len(s)

    ps = set(PrimeSieve(n))
    res = []

    for i in range(n):
        if len(res) == 0 or len(res) != 0 and res[-1] not in ps:
            res.append(s[i])

    return ' '.join(res)
