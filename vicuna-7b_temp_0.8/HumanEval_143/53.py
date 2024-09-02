
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
    # Use a dictionary to store the words and their length
    word_list = {}
    for word in sentence:
        if len(word) in word_list:
            word_list[len(word)] += 1
        else:
            word_list[len(word)] = 1

    # Create an empty list to store the prime words
    prime_words = []
    # Iterate through each word in the sentence
    for word, count in word_list.items():
        # Check if the word is prime
        while count > 1:
            if not is_prime(count):
                break
            count -= 1
        # If the word is prime, append it to the list
        prime_words.append(word)

    # Return the words in the correct order
    return ' '.join(prime_words)
