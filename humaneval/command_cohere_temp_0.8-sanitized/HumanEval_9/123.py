from typing import List, Tuple
def rolling_max(numbers: List[int], cap: int = None) -> List[int]:
    if cap is None:
        cap = len(numbers)
    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_max_list.append(numbers[i])
        else:
            if numbers[i] == rolling_max_list[-1]:
                rolling_max_list.append(rolling_max_list[-1])
            else:
                j = rolling_max_list[-1]
                for k in range(i - 1, -1, -1):
                    if numbers[k] > j:
                        j = numbers[k]
                        rolling_max_list[k + 1:] = rolling_max_list[k + 1:] + [j]
                rolling_max_list[k] = j
    if cap != len(numbers):
        rolling_max_list = rolling_max_list[:cap]
    return rolling_max_list
numbers = [1, 2, 3, 2, 3, 4, 2]