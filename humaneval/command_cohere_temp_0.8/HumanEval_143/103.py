Here's a Python script that solves the given problem with an efficient approach using the `prime` library:
```python
import string
from prime import is_prime

def words_in_sentence(sentence):
    words = sentence.split(' ')
    result = []

    for word in words:
        if is_prime(len(word)):
            result.append(word)

    return ' '.join(result)

# Self-contained code example
if __name__ == "__main__":
    sentence = "This is a test"
    print(words_in_sentence(sentence))

    sentence = "lets go for swimming"
    print(words_in_sentence(sentence))
```

This code snippet efficiently identifies prime-length words within the given sentence and returns them in their original order.

To achieve this, the `is_prime` function from the `prime` library is utilized to check whether a given length is a prime number. This implementation showcases the importance of utilizing specialized libraries to achieve optimal solutions in practical coding challenges.

Ensure the `prime` library is installed to execute the code successfully. You can install it via `pip` with the command below:
```bash
pip install prime
```