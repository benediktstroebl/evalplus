
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
    s = sentence.split(' ')
    a = []
    for i in s:
        if (len(i) == 1 or len(i) == 2) and i.isalpha():
            a.append(i)

        elif len(i) > 2 and i.isalpha():
            prime = True
            for j in range(2, int(i[1]) + 1):
                if int(i) % j == 0:
                    prime = False
                    break
            if prime:
                a.append(i)

    # print(a)
    return ' '.join(a)

