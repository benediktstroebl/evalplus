def vowels_count(s):
    """
    Args:
        s (str): A word represented as a string.

    Returns:
        int: The number of vowels in the word.
           Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    # Your code here.
    # Ensure it handles the test cases described in the prompt.

    # Count the vowels
    count = 0
    for char in s:
        if char in 'aieou':
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
        
    return count