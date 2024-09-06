
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

    res = sentence.split(' ')
    print(res)
    print(len(res))
    res_new = []
    for i in res:
        if len(i) > 1:
            print(i)
            print(len(i))
            if len(i) % 2 == 0:
                res_new.append(i[:len(i) // 2])
                res_new.append(i[len(i) // 2:])
            else:
                res_new.append(i[:len(i) // 2 + 1])
                res_new.append(i[len(i) // 2:])
    return''.join(res_new)


