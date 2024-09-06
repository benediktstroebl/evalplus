
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
    for char in s:
        if char in "aeiou":
            count += 1
        elif char == "y" and s.endswith("y"):
            count += 1
    return count

test_cases = [FIX]

for tc in test_cases:
    input_str = tc
    expected_output = tc.strip().split()

    for i in range(1, len(expected_output)):
        expected_output[i] = expected_output[i].strip()

    result = vowels_count(input_str)

    print("Test case:", tc)
    print("Expected:", expected_output)
    print("Actual:", result)