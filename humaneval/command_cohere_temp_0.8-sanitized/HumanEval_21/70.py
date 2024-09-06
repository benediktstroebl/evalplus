def rescale_to_unit(numbers: List[float]) -> List[float]:
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required for resizing.")
    min_num = min(numbers)
    if min_num == 0:
        raise ValueError("Minimum number cannot be zero.")
    max_num = max(numbers)
    if max_num == 0:
        raise ValueError("Maximum number cannot be zero.")
    rescaled = [(x - min_num) / (max_num - min_num) for x in numbers]
    return rescaled