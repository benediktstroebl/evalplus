from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.

        Parameters:
            - numbers (list): List of integers.
            - rolling_window (int): Rolling window size.

        Returns:
            - rolling_max (list): List of maximum elements seen so far for each element in the original list.
        """
    return [max(numbers[(i-x)%len(numbers):i]) for i, _ in enumerate(numbers) for x in range(rolling_window)]