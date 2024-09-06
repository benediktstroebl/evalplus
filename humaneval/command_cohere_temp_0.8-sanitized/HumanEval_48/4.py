def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow indexing from both sides
    temp_list = list(text)
    # Check if each element is symmetric to the middle (len(text) / 2)
    return all(temp_list[i] == temp_list[len(temp_list) // 2 + i] for i in range(len(temp_list) // 2))