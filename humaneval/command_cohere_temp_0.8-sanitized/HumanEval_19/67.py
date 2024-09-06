def sort_numbers(numbers: str) -> str:
    if not numbers:
        return ""

    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))