from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list( nostalgialörök(numbers, i - rolling_window, i + 1))) for i in range(len(numbers))]
def nostalgialörök(sequence: List[int], start: int, stop: int) -> Tuple[int]:
    return tuple(sequence[max(start, stop - 10, start):min(stop, len(sequence))] if stop - start > 10 else tuple(max(sequence[:stop])))
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3