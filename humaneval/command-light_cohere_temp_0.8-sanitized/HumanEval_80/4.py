def is_happy(s):
    """
    Check if a string is happy or not.
    Returns True if the is happy and False otherwise.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    """
    length = len(s)
    if length < 3:
        return False
    s = s[::-1]  # Reverse string to get rid of the last 3 consecutive distinct characters
    for i in range(0, length - 3):
        if s[i] != s[i + 3]:
            return False
    return True