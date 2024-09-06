from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []  # List to store rolling max elements over time.
    max_so_far = float('-inf')  # Track the max element encountered thus far.
    
    for num in numbers:
        if num > max_so_far:
            rolling_max_list.append(num)  # Add the new max to the rolling max list.
            max_so_far = num  # Update the max element encountered thus far.
    
    return rolling_max_list