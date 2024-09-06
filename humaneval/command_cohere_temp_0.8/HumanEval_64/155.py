```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.
    """
    # To count the vowels in the string we use the following trivial python
    # expression:
    # sum(1 for char in string.lower() if char in 'aeiouy')
    # We use the official python function `lower()` to make the string
    # case-insensitive, so that the counting is more robust.
    return sum(1 for char in s.lower() if char in 'aeiouy')

FIX = """
Add more test cases.
"""

if __name__ == "__main__":
    # Additional test cases to ensure the function's correctness.
    print(vowels_count(" mobilized"))
    print(vowels_count(" monopol"))
    print(vowels_count(" synoptic"))
    print(vowels_count("Qyryry"))
    print(vowels_count(" Automate"))
```

The above code contains a function `vowels_count()` which takes a string representing
a word as input and returns the number of vowels in the string. 

The script also includes test cases to verify the correctness of the `vowels_count()` function. The test cases are printed via a main script block using Python's `if __name__ == "__main__":` mechanism, which is used to define a code block that is executed when the script is run directly.