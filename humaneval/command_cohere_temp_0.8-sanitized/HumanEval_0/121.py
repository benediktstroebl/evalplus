def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y <= threshold for x, y in zip(numbers, numbers[1:]))