
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


    # r1 = [i for i in sentence.split(' ')]
    # r2 = []
    #
    # for i in r1:
    #     if len(i) % 2 == 0 and len(i) > 1:
    #         r2.append(i)
    #
    # r2.sort()
    # r3 = ' '.join(r2)
    # return r3

    s = []
    for w in sentence.split():
        if len(w) % 2 == 0 and len(w) > 1:
            s.append(w)
    return " ".join(s)



































































































