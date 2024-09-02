
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
    words = sentence.split(' ')
    prim_numbers = {1, 2, 3, 5, 7}
    s = set()
    for num in prim_numbers:
        for word in words:
            if len(word) == num:
                s.add(word)
    res = [x for x in words if x in s]
    return ' '.join(res)
