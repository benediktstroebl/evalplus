import unittest
def rescale_to_unit(numbers: List[float]) -> List[float]:
    return (numbers - min(numbers)) / (max(numbers) - min(numbers)) * 0.5 + 0.5