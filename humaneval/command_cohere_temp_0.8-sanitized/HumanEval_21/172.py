def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        raise ValueError("Input list must not be empty")
    try:
        numeric_numbers = [x for x in numbers if isinstance(x, (int, float))]
        if not numeric_numbers:
            raise ValueError("Input list must contain only numeric values")
        return rescale_to_unit_internal(numeric_numbers)
    except ValueError as e:
        return [str(e)] * len(numbers)