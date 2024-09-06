
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
    word_list = []
    for word in words:
        if len(word) > 1:
            is_prime = True
            while len(word) % 2 == 0:
                word = word[:-1]
                is_prime = is_prime and word.is_prime()
                if not is_prime:
                    break
            if word.is_prime():
                word_list.append(word)
    return " ".join(word_list)
