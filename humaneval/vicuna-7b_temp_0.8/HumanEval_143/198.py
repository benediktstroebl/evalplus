
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
    words = sentence.split()
    n = len(words)
    primes = [x for x in range(1, n+1) if x % 2 != 0]
    words_new = []
    for i in range(n):
        for j in range(i+1, n):
            if (j - i) % 2 != 0:
                words_new.append(words[i])
                words_new.append(words[j])
                words_new.append(words[i+1])
                words_new.append(words[j-1])
        if len(words_new[-1]) != 1:
            words_new.append(words[i])
    return " ".join(words_new)
