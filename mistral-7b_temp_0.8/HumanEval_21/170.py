from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # your code here
    low = min(numbers)
    high = max(numbers)
    # try to fix an error
    # check the return type of min() and max()
    # 确保如果输入为空，则low和high的值都是1
    if len(numbers) == 0:
        low, high = 1, 1
    for i in range(len(numbers)):
        # 解决第一个元素是0的情况
        if numbers[i] == low:
            numbers[i] = 0.0
        else:
            numbers[i] = (numbers[i] - low) / (high - low)
    return numbers
