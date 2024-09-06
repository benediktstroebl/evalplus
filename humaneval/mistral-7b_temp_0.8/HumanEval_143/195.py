
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
    # you are welcome to use the "for" keyword in your solution

    # 1. get the list of all the words in the sentence
    words = sentence.split(" ")

    # 2. iterate through the list of words and check if the length of each word is a prime number
    # and append them to a new list if they are
    prime_words = []
    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    # 3. join the words in the new list together with spaces to create the new sentence
    new_sentence = " ".join(prime_words)

    # 4. return the new sentence
    return new_sentence

