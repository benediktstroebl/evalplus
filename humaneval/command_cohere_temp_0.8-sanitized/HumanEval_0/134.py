from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    # Using a dictionary (more efficient) to store numbers as keys and their indices as values
    num_index_dict = {num: index for index, num in enumerate(numbers)}
    
    # Counting the number of elements in the list
    num_count = len(numbers)
    
    # Using a double loop to compare each number with every other number in the list
    for i in range(num_count):
        for j in range(i + 1, num_count):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    
    return False