```python
def is_prime(n):
    """
    Checks whether the number is prime or not.
    :param n: number to check
    :return: boolean
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    :param sentence: input sentence
    :return: string containing words with prime lengths
    """
    words = sentence.split()  # split the sentence into words
    prime_words = []          # list to store prime words

    for word in words:
        if is_prime(len(word)):
            prime_words.append(word)

    return ' '.join(prime_words)  # return joined prime words
```

This script includes the `is_prime` function for checking whether a number is prime or not.

The `words_in_sentence` function first splits the input sentence into individual words using the `split()` method. It then iterates through each word in the sentence and checks if its length is prime using the `is_prime` function. If a word has a prime length, it's added to the `prime_words` list. Finally, the function joins the prime words back together using space as a delimiter and returns the resulting string.

The `prime_words` list is necessary to ensure we only append prime words and maintain the order of the original sentence. 

The output will be as shown in the previous examples, where only words with prime lengths are returned in the original sentence's order. 

This approach enhances code readability and maintains a separation of concerns between primality checking and the main problem.