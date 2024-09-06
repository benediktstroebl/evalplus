
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
    from math import sqrt
    if not sentence:
        return ''

    words = sentence.split()
    prime_nums = []
    for n in range(2, int(sqrt(len(sentence)))+1):
        if n > sqrt(len(sentence)):
            break
        if len(sentence)%n == 0:
            prime_nums.append(n)

    res = []
    for i in range(len(words)):
        if any([True if words[i].count(word) > 1 else False for word in words[i]]):
            continue
        if len(words[i]) in prime_nums:
            res.append(words[i])
    return''.join(res)
