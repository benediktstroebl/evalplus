
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
    # Create a set to store prime numbers
    prime_numbers = set()
    # Create a list to store the words
    words = sentence.split()
    # Keep track of the last word that is added to the new list
    last_word = None
    # Loop through the words
    for word in words:
        if word.isdigit():
            # If the word is a digit, we have reached the end of the sentence
            break
        # Add the word to the list of words
        prime_numbers.add(len(word))
        # Check if the current word is the last word
        if last_word is None:
            last_word = word
        else:
            # If the current word is not the last word
            words.append(last_word)
            # If the current length is not prime, remove it from the list of prime numbers
            if not prime_numbers.pop(0) % (last_word.length + 1):
                # Remove the current word from the list of words
                words.remove(last_word)
                # Add the current word again with the corrected length
                words.append(last_word)
                # Update the last word
                last_word = word
    return ' '.join(words)