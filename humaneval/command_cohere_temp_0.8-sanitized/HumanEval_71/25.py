def triangle_area(a, b, c):
    if not isinstance(a, Iterable) or len(a) != 3:
        return "Error: Input must be an iterable of exactly 3 elements"
    for val in a:
        if not isinstance(val, (int, float)):
            return "Error: Input values must be integers or floats"
    return triangle_area(float(a), float(b), float(c))