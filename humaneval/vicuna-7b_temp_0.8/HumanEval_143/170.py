
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
    result = []
    for word in words:
        if len(word) > 1:
            prime_length = 2
            next_prime_length = 3
            new_word = word
            while next_prime_length <= len(new_word):
                if new_word % next_prime_length == 0:
                    prime_length = next_prime_length + 1
                else:
                    next_prime_length += 2
            if prime_length == len(new_word):
                result.append(new_word)
            else:
                result.append(word)
    return ' '.join(result)