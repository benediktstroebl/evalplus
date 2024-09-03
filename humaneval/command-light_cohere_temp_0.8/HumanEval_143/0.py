```python
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers, the order of the words in the new string should be the same as the original one.

    Constraints:
    * 1 <= len(sentence) <= 100
    * sentence contains only letters (upper or lower)
    * The output string must contain only lowercase letters

    Example:
    Input: 'This is a test"
    Output: "is"

    Example:
    Input: 'abc123abc'
    Output: 'abc123'

    """

    # Get all prime numbers from 2 to the length of the sentence
    prime_nums = [i for i in range(2, len(sentence)) if sentence[i] == sentence[i] == True]

    # Get the index of the first prime number
    # Make sure it's the smallest index possible.
    prime_idx = prime_nums[0]

    # Get all words from the sentence
    words = sentence.split()

    # Get # Join all prime numbers and the first index
    # to get all prime words
    words = [sentence[i] for i in range(prime_idx, len(sentence))]

    # Join all the words into one string
    # while keeping the original order
    return ' '.join(words)
```