from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []  # List to store rolling max elements encountered so far
    
    for n in numbers:
        if n == rolling_max_list[-1]:
            continue  # If current element is same as last rolling max, skip
        
        rolling_max_list.append(n)  # Update rolling max list with current element
        
        # Remove elements that are no longer the rolling max from the front of the list
        while rolling_max_list[0] != rolling_max_list[-1] and rolling_max_list[0] != n:
            rolling_max_list.pop(0)  # Remove the first element of rolling_max_list
    
    return rolling_max_list
numbers = [1, 2, 3, 2, 3, 4, 2]