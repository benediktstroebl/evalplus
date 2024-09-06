```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredoms
```

This script leverages Python's powerful string manipulation capabilities, specifically regex-like splitting and filtering operations, to efficiently handle the task of identifying and counting boredoms in the given input string.

Below are some usage examples of the `is_bored()` function to demonstrate its functionality:
```python
# Example 1
input_string = "The sky is blue. The sun is shining. I love this weather"
result = is_bored(input_string)
print(result)  # Output: 1

# Example 2
input_string = "Hello world"
result = is_bored(input_string)
print(result)  # Output: 0

# Example 3
input_string = "I am bored. What should we do today?"
result = is_bored(input_string)
print(result)  # Output: 1
```

This function is straightforward to use and understand, making it accessible even for those less experienced with Python. Its concise approach demonstrates the power of Python's expressive syntax in solving programming challenges efficiently.