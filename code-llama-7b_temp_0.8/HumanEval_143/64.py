
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
    # 1. Take input
    # 2. Create a list of words in sentence
    # 3. Create a new list of words that are prime length
    # 4. Iterate through new list and add each word to a string
    # 5. Return string
    # 6. Edge Cases

    def is_prime(number):
        if number < 2:
            return False
        for divisor in range(2, number):
            if number % divisor == 0:
                return False
        return True

    def words_in_sentence(sentence):
        words_list = sentence.split()
        prime_words_list = []
        for word in words_list:
            if is_prime(len(word)):
                prime_words_list.append(word)
        return " ".join(prime_words_list)

    return words_in_sentence(sentence)

    # # Test cases
    # print(words_in_sentence("This is a test"))
    # print(words_in_sentence("lets go for swimming"))
    # print(words_in_sentence("code wars"))
