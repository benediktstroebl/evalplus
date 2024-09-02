
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

    sentence = sentence.split(" ")
    result = []
    for word in sentence:
        prime_numbers = []
        if is_prime(len(word)):
            prime_numbers.append(word)
            result.append(prime_numbers[0])
        else:
            for i in range(len(word)):
                if is_prime(i):
                    prime_numbers.append(word[i])
            result.append("".join(prime_numbers))
    return " ".join(result)
