
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
    words_len = len(words)
    prime = [2, 3]
    for i in range(2, words_len):
        for j in range(2, prime[-1]):
            if prime[-1] % j == 0:
                prime.append(j)
                break
    return " ".join(prime[i] for i in range(words_len) if prime[i] == words[i
