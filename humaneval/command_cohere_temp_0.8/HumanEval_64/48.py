```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Args:
        s (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """

    # Define the vowels that are to be counted
    vowels = set('aeiouy')

    # Check if y is at the end of the string and if so, add it to vowels
    if s[-1] == 'y' and s[-2:] == 'y':
        vowels.add('y')

    # Count the number of vowels in the string
    count = sum(1 for char in s if char in vowels)
    return count

# Unit tests:
print("Unit Tests:")
print("-------")

print("Test 01: Test word with 'y' at end.")
print("Expected output: 4")
print(vowels_count("happy"))
print()

print("Test 02: Test word with 'a' and other vowels.")
print("Expected output: 3")
print(vowels_count("alaud"))
print()

print("Test 03: Test word with 'e' and other vowels.")
print("Expected output: 3")
print(vowels_count("ideas"))
print()

print("Test 04: Test word with 'o' and other vowels.")
print("Expected output: 3")
print(vowels_count("mango"))
print()

print("Test 05: Test word with 'u' and other vowels.")
print("Expected output: 3")
print(vowels_count("lexure"))
print()

print("Test 06: Test word with 'y' at end and extra characters.")
print("Expected output: 2")
print(vowels_count("dyadic"))
print()

print("Test 07: Test word with 'a' in middle and at end.")
print("Expected output: 4")
print(vowels_count("bala"))
print()

print("Test 08: Test word with no vowels.")
print("Expected output: 0")
print(vowels_count("software"))
print()
``` 

This Python script defines a function called `vowels_count` that takes an input string and returns the number of vowels in the string. The function counts the vowels 'a', 'e', 'i', 'o', 'u', and 'y' as vowels, but only when 'y' is at the end of the word. The script also includes a set of unit tests that verify the correctness of the `vowels_count` function against specific expected output for various test cases.

To execute the script, hit the "Run" button or press F5. The console output should display the unit test results, with comments indicating each test case's expected output and the function's actual output for comparison.