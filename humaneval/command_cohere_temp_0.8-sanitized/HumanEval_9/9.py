from typing import List, Tuple
def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []  # List to store rolling max elements over time

    # Initialize the rolling max as the first element in the sequence
    rolling_max_list.append(numbers[0])

    for i in range(1, len(numbers)):
        # Check if the current element is greater than the current rolling max
        if numbers[i] > rolling_max_list[-1]:
            rolling_max_list.append(numbers[i])
        elif numbers[i] == rolling_max_list[-1]:
            rolling_max_list.append(numbers[i])

        # If the current element is less than or equal to the current rolling max,
        # it means the rolling max stays the same until a greater element arrives.
        # So, we skip adding the current element to the rolling max list.

    return rolling_max_list
numbers = [1, 2, 3, 2, 3, 4, 2]