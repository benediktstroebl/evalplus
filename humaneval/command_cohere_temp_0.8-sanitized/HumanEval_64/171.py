def vowels_count(s):
    """
    Args:
        s (str): A word represented as a string.

    Returns:
        int: The number of vowels in the word.
             Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    # Your code here.
    # Ensure it adheres to the prompt's specifications.

    # Convert the string to lowercase to handle uppercase vowels and simplify the process
    s = s.lower()
    # Count the vowels without considering 'y' at the end
    vowel_count = s.count("aeiou")
    # Check if the last character is 'y' and add 1 to the count
    if s[-1] == "y":
        vowel_count += 1
    return vowel_count