def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are from 'zero' to 'nine'.
    """
    # Split the input string into a list of numbers
    numbers = input_string.split()
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Join the sorted list of numbers into a string
    sorted_string = ' '.join(sorted_numbers)
    
    return sorted_string