
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False

    # Initialize a variable for current index, where we start comparing the consecutive letters
    current_index = 0

    # Loop through the string and compare the consecutive letters
    while current_index < len(s):
        # Get the next letter
        next_letter = s[current_index]

        # Increment the current index
        current_index += 1

        # Check if the next letter is the same as the previous letter
        if next_letter == s[current_index - 1]:
            # If they are the same, we have to move back to the previous letter
            current_index -= 1

        # If the current and next letters are different, check if they are distinct
        if current_index + 1 < len(s) and s[current_index + 1] != s[current_index]:
            # If they are not distinct, we have to move back to the previous letter
            current_index -= 1

        # If the current and next letters are distinct, increment the current index
        else:
            current_index += 1

    return True