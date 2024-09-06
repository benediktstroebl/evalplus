def sort_numbers(input_str: str) -> str:
    """
    Sorts a space-delimited string of numbers from lowest to highest.
    
    Args:
        input_str (str): Space-delimited string of numbers from 'zero' to 'nine'.
        
    Returns:
        str: Ordered string of numbers.
    """
    numbers = input_str.split()
    
    # Convert string numbers to actual numbers:
    numbers = [int(num) for num in numbers]
    
    # Sort them:
    numbers.sort()
    
    return ' '.join(map(str, numbers))