Here's a Python script that contains a function called `words_in_sentence` that solves the problem you've described:
```python
def is_prime(n):
    """
    Checks whether the integer n is a prime number or not.

    Args:
        n (int): Number to be checked.

    Returns:
        bool: True if n is a prime number, False otherwise.
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

    Args:
        sentence (str): The input sentence.

    Returns:
        str: A sentence with words whose lengths are prime numbers.

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
    words = sentence.split(' ')
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return ' '.join(result)

# Self-contained test cases
print(words_in_sentence("This is a test")) # Output: 'is'
print(words_in_sentence("lets go for swimming")) # Output: 'go for'
```

This script includes a `words_in_sentence` function that takes a sentence as input and returns a modified sentence where only the lengths of the prime-numbered words are preserved.

The prime checking function `is_prime` is also included within the script to ensure the responsiveness of the solution. The `words_in_sentence` function uses this `is_prime` function to filter and construct the desired output. 

The script also includes self-contained test cases to showcase how the function performs on different inputs.