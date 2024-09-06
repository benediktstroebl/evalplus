from typing import List, Tuple
def rolling_max(numbers: List[int], pivot_point: int = None) -> List[int]:
    if pivot_point is not None:
        # Using lazy evaluation strategy
        max_so_far = numbers[pivot_point]
        result = [max_so_far]
        left, right = pivot_point, len(numbers) - 1
        while left < right:
            max_so_far = max(numbers[right], max_so_far, numbers[left])
            result.append(max_so_far)
            left += 1
            right -= 1
        return result
    else:
        # Using regular evaluation strategy
        max_so_far = float('-inf')
        result = []
        for right in range(len(numbers)):
            max_so_far = max(numbers[right], max_so_far)
            result.append(max_so_far)
        return result