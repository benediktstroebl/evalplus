def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    
    Args:
        input_str (str): Space-delimited string of numbers from 'zero' to 'nine'.
        
    Returns:
        str: Space-delimited string of sorted numbers.
    """
    numbers = input_str.split()
    
    # Sort function requires integers, so we cast, then sort, then cast back
    return ' '.join(str(num) for num in sorted(map(int, numbers), reverse=True))