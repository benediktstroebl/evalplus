from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

 Args:
    numbers (List[int]): List of integers to analyze
    rolling_window (int): Window size to consider to compute the rolling maximum

 Returns:
    List[int]: List of rolling maximum elements found until given moment in the sequence
 """
 
    # Initialize output list
    result = [float('-inf') for _ in range(len(numbers))]
  
    # Initialize variables to keep track of the maximum so far and its position
    max_so_far = float('-inf')
    max_so_far_position = 0
  
    # Iterate through the list - this loop is centered around the intuition of the rolling max problem
    for i in range(len(numbers)):
        # Update max_so_far if current number is larger than current max_so_far
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
            max_so_far_position = i
  
        # Update the current result index with the max_so_far
        result[i] = max_so_far
  
    # Return the result
    return result