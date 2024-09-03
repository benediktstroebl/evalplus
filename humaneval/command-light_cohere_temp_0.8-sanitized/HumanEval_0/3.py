from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # sort the list ascending and check for the threshold
    if numbers:
        numbers.sort(reverse = True)
        for i in range(len(numbers)):
            if numbers[i] - threshold < numbers[0]:
                return True
        for i in range(len(numbers)):
            if numbers[i] - numbers[i - 1] > threshold:
                return True
        return False