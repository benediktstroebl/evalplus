```python
def anti_shuffle(s):
    """
    Reorders words in a string to achieve an ordered version.
    Returns a Reorders in a way where words are separated by spaces, and each character is sorted 
    based on its ASCII value and rearranged accordingly.
    Note: The original order of words and spaces is preserved.

    Args:
        string s (required to be a sequence of characters, spaces included)

    Returns:
        string where words are ordered.
    """
    string, where all characters have been sorted in ascending ASCII order
    """
    string = ' '.join(sorted(s))
    return string

# Example test cases
print(anti_shuffle('Hello World!!!'))  # Expected output: 'Hello !!!Wdlor'
print(anti_shuffle('  !@#$%^&*()_+{}<>? bare a test!  # ))  # Expected output: '.h_@#$_! Me^ possible an t all'  ( specially formatted!)
```