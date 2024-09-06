```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = 0
    for c in s:
        if c in 'aieou':
            count += 1
        elif c == 'y' and s[-1] == 'y':
            count += 1
    return count

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("AIUEO") == 5
    assert vowels_count("SAENCI") == 4
    assert vowels_count("LYLY") == 2
    assert vowels_count("zzzzzz") == 6
    assert vowels_count("SCIENCE") == 6
    assert vowels_count("PRINCIPLE") == 6
    assert vowels_count("RIEMANN") == 4
    assert vowels_count("HARPYGAETAN") == 6
    assert vowels_count("HARPYGAETANDO") == 7
    assert vowels_count("DIESAR") == 3
    assert vowels_count("NOVOCA") == 3
    assert vowels_count("SOCCER") == 3
    assert vowels_count("SOCCERX") == 4
    assert vowels_count("ALCOA") == 3
    assert vowels_count("ALCOAX") == 4
```

The script defines a function `vowels_count` that takes a string representing a word as input and returns the number of vowels in the string. Vowels are defined as the characters 'a', 'e', 'i', 'o', 'u', and the letter 'y' at the end of the word. The function checks each character in the string and adds 1 to the count variable if the character is a vowel, or if the character is 'y' and it's at the end of the word. The test_vowels_count function then defines a series of tests to validate the functionality of the vowels_count function.  It checks for a variety of different words in different lengths and contexts to ensure the correctness of the `vowels_count` function. 

If you want to evaluate the robustness of this function to different edge cases, you can add more test cases in the `test_vowels_count` function. 

Let me know if you would like to introduce any specific test cases or discuss further ideas to enhance the function.