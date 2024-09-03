from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize set to store unique integers
    unique_set = set(numbers)
    
    # Convert set back to list
    unique_numbers = list(unique_set)
    
    return unique_numbers