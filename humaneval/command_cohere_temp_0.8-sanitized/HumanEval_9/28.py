from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_length: int) -> List[int]:
    """
    Generate a list of rolling maximum elements observed in the list within the rolling_length window.
    """
    if rolling_length <= 0:
        return []

    res = [num for num in numbers[:rolling_length]]
    for i in range(rolling_length, len(numbers)):
        if numbers[i] > numbers[i - rolling_length]:
            res.append(numbers[i])
        else:
            res.append(numbers[i - rolling_length])
    return res
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_length = 3