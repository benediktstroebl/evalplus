
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
    sentence = sentence.lower()
    words = sentence.split()
    prime_words = []
    for word in words:
        if len(word) > 1:
            for i in range(2, len(word)):
                if is_prime(str(i)) and word[i:i+2] != "11":
                    prime_words.append(word)
                    break
            else:
                prime_words.append(word)
    new_sentence = " ".join(prime_words)
    return new_sentence